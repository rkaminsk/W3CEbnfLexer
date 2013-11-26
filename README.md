# W3C EBNF Lexer

A [pygments][] lexer for the Extended Backus-Naur Format ([EBNF][]) used
by the W3C.

An informal definition of the W3C EBNF format is available at
http://www.w3.org/TR/REC-xml/#sec-notation. Note that the W3C EBNF is
*not* the same as the IETF EBNF format defined in [RFC5234][].

It can be used to produce the following

<div class="highlight highlight-w3c_ebnf"><pre><span class="cm">/* W3C EBNF description of the W3C EBNF grammar */</span>
<span class="cm">/* Source: http://railroad.my28msec.com */</span>

<span class="n">Grammar</span>              <span class="o">::=</span> <span class="n">Production</span><span class="o">*</span><span class="-Break"></span>
<span class="n">Production</span>           <span class="o">::=</span> <span class="n">NCName</span> <span class="s1">&#39;::=&#39;</span> <span class="p">(</span> <span class="n">Choice</span> <span class="o">|</span> <span class="n">Link</span> <span class="p">)</span><span class="-Break"></span>
<span class="n">NCName</span>               <span class="o">::=</span> <span class="cm">/* [http://www.w3.org/TR/xml-names/#NT-NCName] */</span><span class="-Break"></span>
<span class="n">Choice</span>               <span class="o">::=</span> <span class="n">SequenceOrDifference</span> <span class="p">(</span> <span class="s1">&#39;|&#39;</span> <span class="n">SequenceOrDifference</span> <span class="p">)</span><span class="o">*</span><span class="-Break"></span>
<span class="n">SequenceOrDifference</span> <span class="o">::=</span> <span class="p">(</span> <span class="n">Item</span> <span class="p">(</span> <span class="s1">&#39;-&#39;</span> <span class="n">Item</span> <span class="o">|</span> <span class="n">Item</span><span class="o">*</span> <span class="p">))</span><span class="o">?</span><span class="-Break"></span>
<span class="n">Item</span>                 <span class="o">::=</span> <span class="n">Primary</span> <span class="p">(</span> <span class="s1">&#39;?&#39;</span> <span class="o">|</span> <span class="s1">&#39;*&#39;</span> <span class="o">|</span> <span class="s1">&#39;+&#39;</span> <span class="p">)</span><span class="o">?</span><span class="-Break"></span>
<span class="n">Primary</span>              <span class="o">::=</span> <span class="n">NCName</span> <span class="o">|</span> <span class="n">StringLiteral</span> <span class="o">|</span> <span class="n">CharCode</span> <span class="o">|</span> <span class="n">CharClass</span> <span class="o">|</span> <span class="s1">&#39;(&#39;</span> <span class="n">Choice</span> <span class="s1">&#39;)&#39;</span><span class="-Break"></span>
<span class="n">StringLiteral</span>        <span class="o">::=</span> <span class="s1">&#39;&quot;&#39;</span> <span class="p">[</span><span class="o">^</span><span class="l">&quot;</span><span class="p">]</span><span class="o">*</span> <span class="s1">&#39;&quot;&#39;</span> <span class="o">|</span> <span class="s2">&quot;&#39;&quot;</span> <span class="p">[</span><span class="o">^</span><span class="l">&#39;</span><span class="p">]</span><span class="o">*</span> <span class="s2">&quot;&#39;&quot;</span><span class="-Break"></span>
<span class="n">CharCode</span>             <span class="o">::=</span> <span class="s1">&#39;#x&#39;</span> <span class="p">[</span><span class="l">0</span><span class="o">-</span><span class="l">9a</span><span class="o">-</span><span class="l">fA</span><span class="o">-</span><span class="l">F</span><span class="p">]</span><span class="o">+</span><span class="-Break"></span>
<span class="n">CharClass</span>            <span class="o">::=</span> <span class="s1">&#39;[&#39;</span> <span class="s1">&#39;^&#39;</span><span class="o">?</span> <span class="p">(</span> <span class="n">Char</span> <span class="o">|</span> <span class="n">CharCode</span> <span class="o">|</span> <span class="n">CharRange</span> <span class="o">|</span> <span class="n">CharCodeRange</span> <span class="p">)</span><span class="o">+</span> <span class="s1">&#39;]&#39;</span><span class="-Break"></span>
<span class="n">Char</span>                 <span class="o">::=</span> <span class="cm">/* [http://www.w3.org/TR/xml#NT-Char] */</span><span class="-Break"></span>
<span class="n">CharRange</span>            <span class="o">::=</span> <span class="n">Char</span> <span class="s1">&#39;-&#39;</span> <span class="p">(</span> <span class="n">Char</span> <span class="o">-</span> <span class="s1">&#39;]&#39;</span> <span class="p">)</span><span class="-Break"></span>
<span class="n">CharCodeRange</span>        <span class="o">::=</span> <span class="n">CharCode</span> <span class="s1">&#39;-&#39;</span> <span class="n">CharCode</span><span class="-Break"></span>
<span class="n">Whitespace</span>           <span class="o">::=</span> <span class="n">S</span> <span class="o">|</span> <span class="n">Comment</span><span class="-Break"></span>
<span class="n">S</span>                    <span class="o">::=</span> <span class="l">#x9</span> <span class="o">|</span> <span class="l">#xA</span> <span class="o">|</span> <span class="l">#xD</span> <span class="o">|</span> <span class="l">#x20</span><span class="-Break"></span>
<span class="n">Comment</span>              <span class="o">::=</span> <span class="s1">&#39;/*&#39;</span> <span class="p">(</span> <span class="p">[</span><span class="o">^</span><span class="l">*</span><span class="p">]</span> <span class="o">|</span> <span class="s1">&#39;*&#39;</span><span class="o">+</span> <span class="p">[</span><span class="o">^</span><span class="l">*/</span><span class="p">]</span> <span class="p">)</span><span class="o">*</span> <span class="s1">&#39;*&#39;</span><span class="o">*</span> <span class="s1">&#39;*/&#39;</span><span class="-Break"></span>
</pre></div>

## Install

First, ensure that both [setuptools][] and [pygments][] are installed.

Then,  install using `setuptools`. This will use setuptools entrypoint
to install the lexer and make it accessible from pygments

```
python setup.py
```

## Test

Now the lexer can be accessed via pygments.

`pygmentize` can be used to verify that the lexer was properly
installed. Since both W3C and IETF EBNF file formats use the `.ebnf`
extension, it is recommended to explicitly specify the W3C EBNF lexer
using the `-l w3c\_ebnf` argument.

To run `pygmentize` on the provided ebnf.ebnf grammar:

```
pygmentize -f html -l w3c\_ebnf -O full ebnf.ebnf > temp.html
```

and view the results in any browser.


[pygments]: http://pygments.org/
[EBNF]: http://en.wikipedia.org/wiki/Extended_Backus%E2%80%93Naur_Form
[RFC5234]: http://tools.ietf.org/html/rfc5234
