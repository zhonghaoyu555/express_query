#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os, sys
import urllib2, urllib
import json
import hashlib

def send_post(url, data):
	try:
		content_type = 'application/json'
		headers = {'Content-Type': content_type}
		req = urllib2.Request(url, data, headers)
		response = urllib2.urlopen(req)
		the_page = response.read()
	except:
		the_page = None
	return the_page

def send_get(url):
	try:
		req = urllib2.Request(url)
		f = urllib2.urlopen(req)
		html = f.read()
		return html
	except:
		return None

if __name__ == '__main__':
	if len(sys.argv) != 2:
		print 'usage like: ./main.py 880350384879600241'
		sys.exit()
	url = 'http://www.kuaidi100.com/autonumber/autoComNum?text=%s' % (sys.argv[1])
	data = '{}'
	page =  send_post(url, data)
	if page == None:
		print '请求失败'
		sys.exit()
	page = json.loads(page)
	type =  page['auto'][0]['comCode']
	id = page['num']

	url = 'http://www.kuaidi100.com/query?type=%s&postid=%s' % (type, id)
	ret = send_get(url)
	if ret:
		ret = json.loads(ret)
		data = ret['data']
		for info in data:
			print '时间: ', info['time']
			print '事件: ', info['context']
