import streamlit as st


class MultiPage:
    """ Class to generate multiple Streamlit pages using an object
    oriented approach
    """
    # initialise the class, give a argument of app_name, annotate the function
    # with its return value of none
    def __init__(self, app_name) -> None:
        # set pages to be an empty list
        self.pages = []
        # give the app_name method argument the value of app_name
        self.app_name = app_name

        # configure the page using a streamlit method
        st.set_page_config(
            page_title=self.app_name,
            page_icon="🖥️"
        )

    # create a class method
    def app_page(self, title, func) -> None:
        """ Appends title"""
        # add to the empty page list we created earlier - becomes a dictionary
        self.pages.append({"title": title, "function": func})

    # create the method to run the app
    def run(self):
        """Set title and menu names"""
        # create a title for each page - the app name
        st.title(self.app_name)
        # add a sidebar menu to each page - radio buttons labled with the title
        # of the page
        page = st.sidebar.radio('Menu', self.pages,
                                format_func=lambda page: page['title'])
        page['function']()