import html

class DefaultPressEntryRenderer:

    def __init__(self):
        self.newline = '\n' 


    def render(self, press_entry):
        
        rendered_press_entry = self.render_paragraph_start()
        rendered_press_entry += self.render_date(press_entry)
        rendered_press_entry += self.render_description(press_entry)
        rendered_press_entry += self.render_links(press_entry)
        rendered_press_entry += self.render_paragraph_end()

        return rendered_press_entry

    def render_paragraph_start(self):
        paragraph_start = "<!-- wp:paragraph -->" + self.newline
        return paragraph_start + "<p>"

    def render_date(self, press_entry):
        print(press_entry.date)
        date_string = press_entry.date.strftime('%Y/%m/%d')
        return '({0}) '.format(date_string)
    
    def render_description(self, press_entry):
        html_description = ""
        for description in press_entry.description:
            html_description += html.escape(description) + "<br>"
        return html_description
    
    def render_links(self, press_entry):
        html_links = ""
        for link in press_entry.links:
            html_links += self.render_link(link)
            if(link != press_entry.links[-1]):
                html_links += "<br>"
        return html_links


    def render_link(self, link):
        return "<a href=\"{0}\">{0}</a>".format(link)
    
    def render_paragraph_end(self):
        return "</p>" + self.newline + "<!-- /wp:paragraph -->" + self.newline