from needle.cases import NeedleTestCase

class BBCNewsTest(NeedleTestCase):
    def test_masthead(self):
        self.driver.get('http://www.bbc.co.uk/news/')
        self.assertScreenshot('#blq-mast', 'bbc-masthead')