import re


class FilterModule(object):

    def filters(self):
        return {
            'get_contrail_version': self.get_contrail_version,
        }

    def get_contrail_version(self, image_and_tag):
        """
        Function returns contrail version from image-tag in comparable format.
        Returned value is integer looks like 500 (for 5.0 version) or 2002 for
        2002 version.
        If container tag is 'latest' or if the version cannot be evaluated then
        version will be set to 9999.
        If someone changes the naming conventions, he must make changes in this
        function to support these new conventions.
        """
        cver = 9999
        _, _, tag = image_and_tag.rpartition(':')

        if '5.0' in tag:
            cver = 500
        elif '5.1' in tag:
            cver = 510
        else:
            tag_date = re.findall(r"19\d\d|20\d\d", tag)
            if len(tag_date):
                cver = int(tag_date[0])

        return cver
