from unicodedata import normalize


    def normalize_str(text):
        try:
            text = unicode(text, 'utf-8')
        except(NameError, TypeError):
            pass

        text = normalize('NFD', text)
        text = text.encode('ascii', 'ignore')
        text = text.decode('utf-8')
        
        return str(text)
        
