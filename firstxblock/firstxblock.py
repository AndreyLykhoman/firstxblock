"""TO-DO: Write a description of what this XBlock is."""

import pkg_resources
from xblock.core import XBlock
from xblock.fields import Integer, Scope, String, Boolean, JSONField, Dict, List, Set, DateTime
from xblock.fragment import Fragment
from xblockutils.studio_editable import StudioEditableXBlockMixin
from django.template import Context, Template


class FirstXBlock(StudioEditableXBlockMixin, XBlock):
    """
    TO-DO: document what your XBlock does.
    """


    # Fields are defined on the class.  You can access them in your code as
    # self.<fieldname>.

    # TO-DO: delete count, and define your own fields.
    display_name =String( display_name='Message', default="Message", scope=Scope.settings, help="Write a message")
    text_course = String( display_name='Messsge\'s text', default="New text", scope=Scope.settings, help="Write a message")
    can_to_skip = Boolean(display_name="Can to choose", default=False, scope=Scope.settings, help="Can User choose?")
    is_read = Boolean(default=False, scope=Scope.user_state, help="Users choose about skip")


    editable_fields = ('text_course', 'can_to_skip', 'display_name')

    def resource_string(self, path):
        """Handy helper for getting resources from our kit."""
        data = pkg_resources.resource_string(__name__, path)
        return data.decode("utf8")

    # TO-DO: change this view to display your data your own way.
    def student_view(self, context=None):
        """
        The primary view of the FirstXBlock, shown to students
        when viewing courses.
        """
        context_html = self.get_context()
        html = self.render_template("static/html/firstxblock.html", context_html)
        frag = Fragment(html)
        frag.add_css(self.resource_string("static/css/firstxblock.css"))
        frag.add_javascript(self.resource_string("static/js/src/firstxblock.js"))
        frag.initialize_js('SaveIsRead')
        return frag

    def get_context(self):
        return {
            'text_course': self.text_course,
            'can_to_skip': self.can_to_skip,
            'is_read': self.is_read,
        }

    def render_template(self, template_path, context):
        template_str = self.resource_string(template_path)
        template = Template(template_str)
        return template.render(Context(context))




    @XBlock.json_handler
    def save_skip_text(self, data, suffix=''):
        """
        Save read message
        :param data:
        :param suffix:
        :return:
        """
        if data['is_read'] == "True":
            self.is_read = True
        return {'is_read': self.is_read}


    # TO-DO: change this to create the scenarios you'd like to see in the
    # workbench while developing your XBlock.
    @staticmethod
    def workbench_scenarios():
        """A canned scenario for display in the workbench."""
        return [
            ("FirstXBlock",
             """<firstxblock/>
             """),
            ("Multiple FirstXBlock",
             """<vertical_demo>
                <firstxblock/>
                <firstxblock/>
                <firstxblock/>
                </vertical_demo>
             """),
        ]
