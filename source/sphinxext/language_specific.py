"""
Copyright (c) 2013, Space Telescope Science Institute
All rights reserved.

Redistribution and use in source and binary forms, with or without modification,
are permitted provided that the following conditions are met:

  Redistributions of source code must retain the above copyright notice, this
  list of conditions and the following disclaimer.

  Redistributions in binary form must reproduce the above copyright notice, this
  list of conditions and the following disclaimer in the documentation and/or
  other materials provided with the distribution.

  Neither the name of the Space Telescope Science Institute nor the
  names of its contributors may be used to endorse or promote products
  derived from this software without specific prior written
  permission.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND
ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE FOR
ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES
(INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON
ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
(INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS
SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
"""

from docutils import nodes
from docutils import statemachine
from sphinx.util.compat import Directive


class AttrDict(dict):
    def __init__(self, *args, **kwargs):
        super(AttrDict, self).__init__(*args, **kwargs)
        self.__dict__ = self


def split_content(l):
    parts = []
    part = []
    language = None

    def add_part():
        if language is None:
            raise ValueError("No language specified")
        parts.append(AttrDict({
            'language': language,
            'content': part}))

    for line in l:
        if line.startswith('--'):
            if len(part):
                add_part()
                part = []
            language = line[2:].strip()
        else:
            part.append(line)

    add_part()

    return parts


class language_specific_pages(nodes.Element):
    local_attributes = ['parts']

    def __init__(self, *args, **kwargs):
        self.parts = kwargs['parts']
        nodes.Element.__init__(self, *args, **kwargs)


def visit_language_specific_pages_node_html(self, node):
    node['classes'] = ['tabbable']

    ul = nodes.bullet_list()
    ul['classes'] = ['nav', 'nav-tabs']
    # set_source_info(self, ul)

    href = tab('', 'Ovation API:')
    href['classes'] = ['disabled']
    paragraph = nodes.paragraph('', '')
    li = nodes.list_item('')
    li['classes'] = ['disabled']

    paragraph.append(href)
    li.append(paragraph)
    ul.append(li)

    first = True
    for part in node.parts:
        href = tab(part.language, part.language)
        href['refuri'] = '#' + make_id(node, part.language)
        paragraph = nodes.paragraph('')
        li = nodes.list_item('')
        if first:
            li['classes'].append('active')

        paragraph.append(href)
        li.append(paragraph)
        ul.append(li)

        first = False

    node.append(ul)

    pages = nodes.admonition()
    pages['classes'] = ['tab-content']

    first = True
    for part in node.parts:
        page = nodes.admonition()
        page['classes'] = ['tab-pane']
        if first:
            page['classes'].append('active')
        page['ids'] = [make_id(node, part.language)]

        page.append(part.paragraph)
        pages.append(page)

        first = False

    node.append(pages)

    self.body.append(self.starttag(node, 'div'))


def depart_language_specific_pages_node_html(self, node):
    self.body.append('</div>')


def visit_language_specific_pages_node_latex(self, node):
    for part in node.parts:
        t = tab('', '')
        t.language = part.language
        t.append(part.paragraph)
        node.append(t)


def depart_language_specific_pages_node_latex(self, node):
    pass


class tab(nodes.General, nodes.Inline, nodes.Referential, nodes.TextElement):
    pass


def visit_tab_node_html(self, node):
    atts = {}
    if 'refuri' in node:
        atts['href'] = node['refuri']
        atts['data-toggle'] = 'tab'
    self.body.append(self.starttag(node, 'a', '', **atts))


def depart_tab_node_html(self, node):
    self.body.append('</a>')


def visit_tab_node_latex(self, node):
    self.body.append(r'\begin{jsonframe}{%s}{black}' % node.language)


def depart_tab_node_latex(self, node):
    self.body.append(r'\end{jsonframe}')


def make_id(self, language):
    return '{0}_{1}'.format(hex(id(self))[2:], language)


class LanguageSpecificDirective(Directive):
    has_content = True

    def run(self):
        parts = split_content(self.content)
        container = language_specific_pages(parts=parts)

        for part in parts:
            paragraph = nodes.paragraph('', '')
            content = statemachine.StringList(part.content)
            content.parent = self.content.parent
            self.state.nested_parse(content, 0, paragraph)
            part.paragraph = paragraph

        return [container]


def setup(app):
    app.add_node(tab,
                 html=(visit_tab_node_html, depart_tab_node_html),
                 latex=(visit_tab_node_latex, depart_tab_node_latex))
    app.add_node(language_specific_pages,
                 html=(visit_language_specific_pages_node_html,
                       depart_language_specific_pages_node_html),
                 latex=(visit_language_specific_pages_node_latex,
                        depart_language_specific_pages_node_latex))

    app.add_directive('language_specific', LanguageSpecificDirective)


latex_preamble = r"""
  \usepackage{mdframed}
  \usepackage{tikz}

  \newenvironment{jsonframe}[2]{%
  \ifstrempty{#1}%
  {}%
  {\mdfsetup{%
    frametitle={%
    \tikz[baseline=(current bounding box.east),outer sep=0pt,text=white]
    \node[anchor=east,rectangle,fill=#2]
    {\strut #1};}}%
   }%
   \mdfsetup{innertopmargin=10pt,linecolor=#2,%
             linewidth=1pt,topline=true,nobreak=true,
             frametitleaboveskip=\dimexpr-\ht\strutbox\relax,}
   \begin{mdframed}[]\relax%
   }{\end{mdframed}}
"""
