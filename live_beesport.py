# -*- coding: utf-8 -*-
# @Author  : Doubebly
# @Time    : 2025/5/19 21:19

import sys
import os
sys.path.append('..')
from base.spider import Spider


class Spider(Spider):
    def getName(self):
        return "BeeSport"

    def init(self, extend):
        self.ext_time = 120
        self.cache_path = '/storage/emulated/0/TV/cache_BeeSport'
        if not os.path.exists(self.cache_path):
            os.mkdir(self.cache_path, 0o755)

    def getDependence(self):
        return []

    def isVideoFormat(self, url):
        # You can implement format checks here if needed
        return url.endswith(".m3u8") or url.endswith(".mp4")

    def manualVideoCheck(self):
        # Optional manual check implementation
        return False

    def liveContent(self, url):
        data_list = [
            {
                'tvg-id': '',
                'tvg-name': '',
                'tvg-logo': 'https://logo.doube.eu.org/beesport/TNT_SPORTS_1.png',
                'group-title': 'BeeSport',
                'name': 'TNT SPORTS 1',
                'fun': 'beesport',
                'pid': 'TNT_Sports_1'
            },
            # ... (other channels, keep as in your version)
        ]

        tv_list = ['#EXTM3U']
        for i in data_list:
            tvg_id = i['tvg-id']
            tvg_name = i['tvg-name']
            tvg_logo = i['tvg-logo']
            group_name = i['group-title']
            name = i['name']
            fun = i['fun']
            pid = i['pid']
            tv_list.append(
                f'#EXTINF:-1 tvg-id="{tvg_id}" tvg-name="{tvg_name}" '
                f'tvg-logo="{tvg_logo}" group-title="{group_name}",{name}'
            )
            tv_list.append(
                f'{self.getProxyUrl()}&fun={fun}&pid={pid}&Author=Doubebly&TG=t.me/doubebly001'
            )

        return '\n'.join(tv_list)

    def homeContent(self, filter):
        # Optional: return home categories
        return {"class": [], "filters": {}}

    def homeVideoContent(self):
        # Optional: return homepage videos
        return []

    def categoryContent(self, tid, pg, filter, extend):
        # Optional: category listing
        return {"list": [], "page": pg, "pagecount": 1, "limit": 20, "total": 0}

    def detailContent(self, array):
        # Optional: detail page content
        return {"list": []}

    def searchContent(self, key, quick):
        # Optional: search results
        return {"list": []}
