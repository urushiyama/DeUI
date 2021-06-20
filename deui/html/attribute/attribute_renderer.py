class AttributeRenderer:
    """
    This class handles rendering attributes produced by attribute builders which are passed when initiated.
    """
    def __init__(self, *args):
        self.builders = set(builder for builder in args if hasattr(builder, 'build_attributes'))

    def attributes(self, html_widget):
        """
        Renders attributes produced by attribute builders which are passed when initiated.

        Args:
            html_widget (HTMLWidget): a HTML widget class instance that has attributes to build.

        Return:
            (str): attributes list that can be embedded in HTML tag.
        """
        result = ""

        for builder in self.builders:
            result += builder.build_attributes(html_widget)

        return result
