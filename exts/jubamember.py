#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""

Jubatus Member Extension
========================

Copyright (C) 2013 Jubatus Team

Usage
-----

.. jubamember::
   :name: Your Name
   :photo: http://example.com/photo.png
   :role: Developer
   :contrib: Project Management, Core Development
   :github: account_name
   :twitter: account_name
   :web: http://www.example.com/
   :blog: http://blog.example.com/
   :email: me@example.com

Note that "name", "photo", "role", and "contrib" are mandatory. Others are optional.

"""

from docutils import nodes
from docutils.parsers.rst import directives

from sphinx.util.compat import Directive

class jubamember(nodes.General, nodes.Element):
    pass

def html_visit_jubamember_node(self, node):
    member_box = u""

    # Header
    member_box += u"""
        <div class="member-box">
          <div class="member-photo">
            <img src="%s">
          </div>
          <div class="member-details">
            <div><span class="member-name">%s</span> ― %s</div>
            <div class="member-relation">
              <div class="member-contrib">%s</div>
              <ul class="member-social">
    """ % (node['photo'], node['name'], node['role'], node['contrib'])

    # Social Links
    if 'github' in node:
        member_box += u"""
                <li class="github"><a href="https://github.com/%s">GitHub</a></li>
        """ % (node['github'])
    if 'twitter' in node:
        member_box += u"""
                <li class="twitter"><a href="http://twitter.com/%s">Twitter</a></li>
        """ % node['twitter']
    if 'web' in node:
        member_box += u"""
                <li class="web"><a href="%s">Web</a></li>
        """ % node['web']
    if 'blog' in node:
        member_box += u"""
                <li class="blog"><a href="%s">Blog</a></li>
        """ % node['blog']
    if 'email' in node:
        member_box += u"""
                <li class="mail"><a href="mailto:%s">Email</a></li>
        """ % node['email']

    # Footer
    member_box += u"""
              </ul>
            </div>
          </div>
          <div style="clear: left;"></div>
        </div>
    """
    self.body.append(member_box)

def html_depart_jubamember_node(self, node):
    pass

class JubatusMemberDirective(Directive):
    has_content = False
    required_arguments = 0
    optional_arguments = 0
    final_argument_whitespace = True
    option_spec = {
        'name': unicode,
        'photo': directives.uri,
        'role': unicode,
        'contrib': unicode,
        'github': directives.uri,
        'twitter': directives.uri,
        'web': directives.uri,
        'blog': directives.uri,
        'email': directives.uri,
    }

    def run(self):
        node = jubamember()
        for key in self.options:
            node[key] = self.options[key]
        for key in ['name', 'photo', 'role', 'contrib']:
            if not key in node:
                return [self.state.document.reporter.error("Required key %s not found" % key, line=self.lineno)]
        return [node]

def setup(app):
    app.add_node(jubamember, html=(html_visit_jubamember_node, html_depart_jubamember_node))
    app.add_directive('jubamember', JubatusMemberDirective)
