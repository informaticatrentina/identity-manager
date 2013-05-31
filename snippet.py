def general_callback(resource, request, payload):
    print 'A GET on the "%s" endpoint was just performed!' % resource
    app.logger.debug('A GET on the "%s" endpoint was just performed!', resource)
    1/0

app.on_get += general_callback

def before_post(resource, documents):
    print 'About to store documents to "%s" ' % resource
    app.logger.info('A POST on the "%s" endpoint for the document %s was just performed!', resource, documents)
    1/0

app.on_posting += before_post

