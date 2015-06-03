from burp import IBurpExtender
from burp import IMessageEditorTabFactory
from burp import IMessageEditorTab
from burp import IParameter
from burp import IHttpRequestResponse

import java.io
import java.util.zip
import org.python.util

import zlib
import java.io.ByteArrayOutputStream
import java.io.ByteArrayInputStream
import java.io.ObjectInputStream
import java.io.ObjectOutput
import java.io.ObjectOutputStream
import org.python.util.PythonObjectInputStream
import java.lang.RuntimeException

# import external Jars
import sys
from os import listdir
from os.path import join

extends_jars = lambda path: [join(path, jar) for jar in listdir(path) if jar.endswith(".jar")]
sys.path.extend(extends_jars(sys.path[-1]))


import com.thoughtworks.xstream.XStream
import com.thoughtworks.xstream.io.xml.DomDriver

class BurpExtender(IBurpExtender, IMessageEditorTabFactory):

    #
    # implement IBurpExtender
    #
    def registerExtenderCallbacks(self, callbacks):

        # keep a reference to our callbacks object
        self._callbacks = callbacks

        # obtain an extension helpers object
        self._helpers = callbacks.getHelpers()

        # set our extension name
        callbacks.setExtensionName("Java Serialized XML viewer")

        # register ourselves as a message editor tab factory
        callbacks.registerMessageEditorTabFactory(self)

        return

    #
    # implement IMessageEditorTabFactory
    #
    def createNewInstance(self, controller, editable):

        # create a new instance of our custom editor tab
        return JavaSerializeXMLInputTab(self, controller, editable)

#
# class implementing IMessageEditorTab
#
class JavaSerializeXMLInputTab(IMessageEditorTab):

    def __init__(self, extender, controller, editable):
        self._extender = extender
        self._editable = editable


        # create an instance of Burp's text editor, to display our deserialized data
        self._txtInput = extender._callbacks.createTextEditor()
        self._txtInput.setEditable(False)
        return

    #
    # implement IMessageEditorTab
    #
    def getTabCaption(self):
        return "Java Serialized XML viewer"

    def getUiComponent(self):
        return self._txtInput.getComponent()

    def isEnabled(self, content, isRequest):
        # enable this tab for requests containing a data parameter
        #return isRequest and not self._extender._helpers.getRequestParameter(content, "data") is None
        return True

    def setMessage(self, content, isRequest):
        if (content is None):
            print "content none"
            # clear our display
            self._txtInput.setText(None)
            self._txtInput.setEditable(False)

        else:
            # retrieve the data parameter
            request_info = self._extender._helpers.analyzeRequest(content)
            bodyoffset = request_info.getBodyOffset()

            payload_serialized_deflate = content[bodyoffset:]
            payload_serialized_inflate = zlib.decompress(payload_serialized_deflate)

            byte_array  = java.io.ByteArrayInputStream(payload_serialized_inflate)

            try:
                py_stream = org.python.util.PythonObjectInputStream(byte_array).readObject()
            except java.lang.RuntimeException, e:
                self._txtInput.setText("Erreur lors de la tentative de deserialization du contenu")
                self._currentMessage = content
                return

            xstream = com.thoughtworks.xstream.XStream(com.thoughtworks.xstream.io.xml.DomDriver())
            xml_deserialized = xstream.toXML(i)

            # deserialize the parameter value
            self._txtInput.setText(xml_deserialized)
            self._txtInput.setEditable(False)

        # remember the displayed content
        self._currentMessage = content
        return

    def getMessage(self):
        # determine whether the user modified the deserialized data
        if (self._txtInput.isTextModified()):
            # reserialize the data
            text = self._txtInput.getText()
            payload_serialized_deflate = zlib.compress(text)

            new_request_body = payload_serialized_deflate

            request_info = self._extender._helpers.analyzeRequest(self._currentMessage)

            new_http_message = self._extender._helpers.buildHttpMessage(request_info.getHeaders(), new_request_body)
            return new_http_message
        else:
            return self._currentMessage

    def isModified(self):
        return self._txtInput.isTextModified()

    def getSelectedData(self):
        return self._txtInput.getSelectedText()
