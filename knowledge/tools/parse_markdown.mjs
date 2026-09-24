#!/usr/bin/env node
// One structural parser for every subsequent Machine KB projection.
process.on('uncaughtException', error => { console.error(error.message); process.exitCode = 1; });
import { lexer } from './vendor/marked/marked.mjs';
let input = '';
for await (const part of process.stdin) input += part;
const { records, identities, bootstrap } = JSON.parse(input);
const fail = (path, detail) => { throw new Error(`${path}: ${detail}`); };
const cues = {
  applicability: /\b(?:SCS|ZigBee|TCP|gateway|firmware|revision|version|only for|applies to|not applicable)\b/gi,
  cautions: /\b(?:caution|warning|do not|must not|avoid|limitation|not evidence|cannot infer)\b/gi,
  uncertainty: /\b(?:unknown|unresolved|unclear|hypothes(?:is|ized)|appears|may|might|not established|not verified|contradict(?:ory|s|ion)?)\b/gi,
  provenance_references: /\b(?:source|evidence|catalogue|database|specification|capture|experiment|documentation)\b/gi,
};
function annotations(text) {
  return Object.fromEntries(Object.entries(cues).map(([key, regex]) =>
    [key, [...new Set([...text.matchAll(regex)].map(m => m[0].toLowerCase()))].sort()]));
}
function inline(tokens, path) {
  return (tokens ?? []).map(t => {
    switch (t.type) {
      case 'text': case 'escape': case 'codespan': return { type:t.type, text:t.text };
      case 'strong': case 'em': case 'del': return { type:t.type, children:inline(t.tokens,path) };
      case 'link': case 'image': return { type:t.type, target:t.href, title:t.title ?? '', text:t.text, children:inline(t.tokens,path) };
      case 'br': return { type:'break' };
      default: return fail(path, `unsupported inline construct ${t.type}`);
    }
  });
}
const links = nodes => nodes.flatMap(n => n.type === 'link' || n.type === 'image'
  ? [{ target:n.target, title:n.title, text:n.text, type:n.type }, ...links(n.children)]
  : n.children ? links(n.children) : []);
function blockLinks(block) {
  if (block.inline) return links(block.inline);
  if (block.type === 'table') return links([...block.header,...block.rows.flat()].flatMap(c=>c.inline));
  if (block.type === 'list') return block.items.flatMap(i=>i.blocks.flatMap(blockLinks));
  if (block.type === 'blockquote') return block.blocks.flatMap(blockLinks);
  return [];
}
function blocks(tokens, path, startLine=1) {
  let line = startLine;
  const result = [];
  for (const t of tokens) {
    const at = line; line += (t.raw?.match(/\n/g) ?? []).length;
    const base = { line:at };
    switch(t.type) {
      case 'space': continue;
      case 'heading': result.push({ ...base, type:'heading', level:t.depth, text:t.text, inline:inline(t.tokens,path) }); break;
      case 'paragraph': case 'text': result.push({ ...base, type:'paragraph', text:t.text, inline:inline(t.tokens,path) }); break;
      case 'code': result.push({ ...base, type:'code', language:t.lang ?? '', text:t.text }); break;
      case 'table': result.push({ ...base, type:'table', align:t.align, header:t.header.map(c=>({ text:c.text, inline:inline(c.tokens,path) })), rows:t.rows.map(row=>row.map(c=>({ text:c.text, inline:inline(c.tokens,path) }))) }); break;
      case 'list': result.push({ ...base, type:'list', ordered:t.ordered, start:t.start ?? null, items:t.items.map(i=>({ checked:i.checked ?? null, blocks:blocks(i.tokens,path,at) })) }); break;
      case 'blockquote': result.push({ ...base, type:'blockquote', blocks:blocks(t.tokens,path,at) }); break;
      case 'hr': result.push({ ...base, type:'rule' }); break;
      case 'html': fail(path, `unsupported raw HTML at line ${at}`); break;
      default: fail(path, `unsupported block construct ${t.type} at line ${at}`);
    }
  }
  return result;
}
const slug = s => s.toLowerCase().replace(/<[^>]*>/g,'').replace(/[^a-z0-9]+/g,'-').replace(/^-|-$/g,'') || 'section';
function context(path) {
  const area = path.split('/')[0];
  const match = path.match(/^functional\/who-(\d+)(?:-|\/)/);
  return { area, namespace:match ? `who:${match[1]}` : area === 'diagnostics' ? 'diagnostic' : area === 'protocol' ? 'protocol' : 'contextual' };
}
const documents = [];
let nextDoc = Object.keys(identities).length + 1;
for (const rec of records) {
  const path = rec.source_path;
  if (!rec.privacy || !['public','sanitized'].includes(rec.privacy.classification)) fail(path,'unpublishable privacy classification');
  if (path.startsWith('guides/')) fail(path,'guide source entered canonical parser');
  const parsed = blocks(lexer(rec.text, { gfm:true }),path);
  let entry = identities[path];
  if (!entry) {
    if (!bootstrap) fail(path,'missing curated document identity');
    entry = { id:`ownkb:document:d${String(nextDoc++).padStart(6,'0')}`, sections:{} }; identities[path] = entry;
  }
  const sections = []; const stack = []; const seen = {};
  for (const b of parsed) {
    if (b.type !== 'heading') {
      if (!sections.length) {
        if (!entry.sections['@preamble']) {
          if (!bootstrap) fail(path,'missing preamble identity');
          entry.sections['@preamble'] = `${entry.id.replace('document','section')}:s000000`;
        }
        sections.push({ id:entry.sections['@preamble'], anchor:'@preamble', level:0, title:'', parent:null, blocks:[], children:[] });
      }
      const section = stack.at(-1) ?? sections[0];
      const content = b.text ?? JSON.stringify(b.type === 'table' ? [b.header,b.rows] : b.type === 'list' ? b.items : b.type === 'blockquote' ? b.blocks : '');
      section.blocks.push({ ...b, ...annotations(content), links:blockLinks(b), privacy:rec.privacy });
      continue;
    }
    const label = slug(b.text); seen[label] = (seen[label] ?? 0) + 1;
    const anchor = `${label}-${seen[label]}`;
    let id = entry.sections[anchor];
    if (!id) {
      if (!bootstrap) fail(path,`missing curated section identity for ${anchor}`);
      id = `${entry.id.replace('document','section')}:s${String(Object.keys(entry.sections).length+1).padStart(6,'0')}`;
      entry.sections[anchor] = id;
    }
    while (stack.length && stack.at(-1).level >= b.level) stack.pop();
    const section = { id, anchor, level:b.level, title:b.text, title_inline:b.inline, parent:stack.at(-1)?.id ?? null, blocks:[], children:[] };
    if (stack.length) stack.at(-1).children.push(id);
    sections.push(section); stack.push(section);
  }
  const used = new Set(sections.map(s=>s.anchor));
  for (const key of Object.keys(entry.sections)) if (!used.has(key)) fail(path,`stale curated section anchor ${key}; update mapping while retaining ID`);
  const namespace_context = context(path);
  for (const section of sections) {
    section.privacy = rec.privacy;
    section.namespace_context = namespace_context;
    section.provenance = { source_id:rec.source_id, document_id:entry.id, section_id:section.id, path, evidence_class:'canonical_documentation' };
  }
  documents.push({ id:entry.id, path, source_id:rec.source_id, privacy:rec.privacy, namespace_context, sections });
}
documents.sort((a,b)=>a.id < b.id ? -1 : a.id > b.id ? 1 : 0);
process.stdout.write(JSON.stringify({ format:'ownkb-ir-0.1.0', documents, identities })+'\n');
