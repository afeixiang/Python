#!/usr/bin/python
# -*- coding: UTF-8 -*-

import xml.sax

class MovieHandler( xml.sax.ContentHandler ):
   def __init__(self):
      self.CurrentData = ()
      self.type = ""
      self.format = ""
      self.year = ""
      self.rating = ""
      self.stars = ""
      self.description = ""

   # 元素开始事件处理
   def startElementNS(self, tag, qname, attributes):
      self.CurrentData = tag
      if tag[1] == "Executable":
         print("*****Executable*****")
         title = attributes.getValueByQName('DTS:refId')         
         print("refId:"+title)
      elif tag[1] == "SqlTaskData":
            print("****SqlTaskData****")
            title = attributes.getValueByQName('SQLTask:SqlStatementSource')
            print("SqlStatementSource:"+title)
      #else:
         #print(self.CurrentData)
         #print(attributes)

   # 元素结束事件处理
   def endElementNS(self, tag, qname):
      if self.CurrentData[1] == "type":
         print("Type:"+self.type)
      elif self.CurrentData[1]== "format":
         print("Format:"+self.format)
      elif self.CurrentData[1]== "year":
         print("Year:"+self.year)
      elif self.CurrentData[1]== "rating":
         print("Rating:"+self.rating)
      elif self.CurrentData[1]== "stars":
         print("Stars:"+self.stars)
      elif self.CurrentData[1]== "description":
         print("Description:"+self.description)
      self.CurrentData= ('','')

   # 内容事件处理
   def characters(self, content):
      if self.CurrentData[1]== "type":
         self.type = content
      elif self.CurrentData[1]== "format":
         self.format = content
      elif self.CurrentData[1]== "year":
         self.year = content
      elif self.CurrentData[1]== "rating":
         self.rating = content
      elif self.CurrentData[1]== "stars":
         self.stars = content
      elif self.CurrentData[1]== "description":
         self.description = content

if ( __name__ == "__main__"):
   # 创建一个 XMLReader
   parser = xml.sax.make_parser()
   # turn off namepsaces
   parser.setFeature(xml.sax.handler.feature_namespaces, 1)
   # 重写 ContextHandler
   Handler = MovieHandler()
   parser.setContentHandler( Handler )
   parser.parse("dts.xml")
