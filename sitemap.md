---
Created On: '2023-04-13T14:48:00+00:00'
Description: ''
Last Edited: '2023-04-13T14:53:00+00:00'
Published On: null
Slug: sitemap
Slug Override: ''
Status: Published
Tags: []
Title: Sitemap
Type: Page
notion_id: 38ce9ad1-b99e-4aaa-b30e-2ae99dd0a326
notion_url: https://www.notion.so/Sitemap-38ce9ad1b99e4aaab30e2ae99dd0a326
---
<div class="sourceCode" id="cb1"><pre class="sourceCode xml"><code class="sourceCode xml"><span id="cb1-1"><a href="#cb1-1" aria-hidden="true" tabindex="-1"></a><span class="fu">&lt;?xml</span><span class="ot"> version=</span><span class="st">&quot;1.0&quot;</span><span class="ot"> encoding=</span><span class="st">&quot;UTF-8&quot;</span><span class="fu">?&gt;</span></span>
<span id="cb1-2"><a href="#cb1-2" aria-hidden="true" tabindex="-1"></a>&lt;<span class="kw">rss</span><span class="ot"> version=</span><span class="st">&quot;2.0&quot;</span><span class="ot"> xmlns:atom=</span><span class="st">&quot;http://www.w3.org/2005/Atom&quot;</span>&gt;</span>
<span id="cb1-3"><a href="#cb1-3" aria-hidden="true" tabindex="-1"></a>    &lt;<span class="kw">channel</span>&gt;</span>
<span id="cb1-4"><a href="#cb1-4" aria-hidden="true" tabindex="-1"></a>        &lt;<span class="kw">atom:link</span><span class="ot"> href=</span><span class="st">&quot;https://goodlifeodyssey.com/rssmain.xml&quot;</span><span class="ot"> rel=</span><span class="st">&quot;self&quot;</span><span class="ot"> type=</span><span class="st">&quot;application/rss+xml&quot;</span> /&gt;</span>
<span id="cb1-5"><a href="#cb1-5" aria-hidden="true" tabindex="-1"></a>        &lt;<span class="kw">title</span>&gt;Good Life Odyssey&lt;/<span class="kw">title</span>&gt;</span>
<span id="cb1-6"><a href="#cb1-6" aria-hidden="true" tabindex="-1"></a>        &lt;<span class="kw">link</span>&gt;https://goodlifeodyssey.com&lt;/<span class="kw">link</span>&gt;</span>
<span id="cb1-7"><a href="#cb1-7" aria-hidden="true" tabindex="-1"></a>        &lt;<span class="kw">description</span>&gt;We are on a long journey to find and live the good life. For most of us, our destination is behind a haze, and we must navigate while traveling. This website is my logbook of landings within philosophy, religion, literature, and history.&lt;/<span class="kw">description</span>&gt;</span>
<span id="cb1-8"><a href="#cb1-8" aria-hidden="true" tabindex="-1"></a>        {%- for p in databases[&#39;Entries&#39;] -%}</span>
<span id="cb1-9"><a href="#cb1-9" aria-hidden="true" tabindex="-1"></a>				{%- if p.Status == &quot;Published&quot; and p.Type in [&quot;Essay&quot;, &quot;Dialogue&quot;, &quot;Meditation&quot;, &quot;Poem&quot;] -%}</span>
<span id="cb1-10"><a href="#cb1-10" aria-hidden="true" tabindex="-1"></a>            &lt;<span class="kw">item</span>&gt;</span>
<span id="cb1-11"><a href="#cb1-11" aria-hidden="true" tabindex="-1"></a>                &lt;<span class="kw">title</span>&gt;{{page.Title}}&lt;/<span class="kw">title</span>&gt;</span>
<span id="cb1-12"><a href="#cb1-12" aria-hidden="true" tabindex="-1"></a>                &lt;<span class="kw">description</span>&gt;{{page.Description}}&lt;/<span class="kw">description</span>&gt;</span>
<span id="cb1-13"><a href="#cb1-13" aria-hidden="true" tabindex="-1"></a>                &lt;<span class="kw">link</span>&gt;https://goodlifeodyssey.com/{{page.Slug}}&lt;/<span class="kw">link</span>&gt;</span>
<span id="cb1-14"><a href="#cb1-14" aria-hidden="true" tabindex="-1"></a>                &lt;<span class="kw">guid</span><span class="ot"> isPermaLink=</span><span class="st">&quot;true&quot;</span>&gt;https://goodlifeodyssey.com/{{page.Slug}}&lt;/<span class="kw">guid</span>&gt;</span>
<span id="cb1-15"><a href="#cb1-15" aria-hidden="true" tabindex="-1"></a>                &lt;<span class="kw">pubDate</span>&gt;{{page[&quot;Published On&quot;]|date_to_rfc822}}&lt;/<span class="kw">pubDate</span>&gt;</span>
<span id="cb1-16"><a href="#cb1-16" aria-hidden="true" tabindex="-1"></a>            &lt;/<span class="kw">item</span>&gt;</span>
<span id="cb1-17"><a href="#cb1-17" aria-hidden="true" tabindex="-1"></a>        {%- endif %}</span>
<span id="cb1-18"><a href="#cb1-18" aria-hidden="true" tabindex="-1"></a>        {%- endfor %}</span>
<span id="cb1-19"><a href="#cb1-19" aria-hidden="true" tabindex="-1"></a>        {%- endfor %}</span>
<span id="cb1-20"><a href="#cb1-20" aria-hidden="true" tabindex="-1"></a>    &lt;/<span class="kw">channel</span>&gt;</span>
<span id="cb1-21"><a href="#cb1-21" aria-hidden="true" tabindex="-1"></a>&lt;/<span class="kw">rss</span>&gt;</span></code></pre></div>
