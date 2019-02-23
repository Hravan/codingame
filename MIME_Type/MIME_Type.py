def find_extension(file_name):
    '''Consume a filename and return its extension in all lowercase letters.
       Return `UNKNOWN` if there is no extension provided.'''

    dot = file_name.rfind('.')
    if dot == -1:
        return 'UNKNOWN'
    else:
        return file_name[dot + 1:].lower()

def find_mime_type(ext, mime_dict):
    '''Consume an extension name and a dictionary that maps extensions to their MIME
       types and return MIME type when it's found, `UNKNOWN` otherwise.'''
    return mime_dict.get(ext, 'UNKNOWN')
