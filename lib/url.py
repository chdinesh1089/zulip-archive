'''
Sometimes it feels like 80% of the battle with creating a
static website is getting all the URLs correct.

These are some helpers.

Here are some naming conventions for URL pieces:

    zulip_url: https://example.zulip.com
    site_url: https://example.zulip-archive.com
    html_root: archive

And then URLs use Zulip stream/topics, which are sometimes
"sanitized" to guarantee uniqueness and not have special characters:

    stream_id: 599
    stream_name: general
    topic_name: lunch

    sanitized_stream_name : 599general
    sanitized_topic_name: 222lunch
'''

import urllib

def zulip_post_url(zulip_url, stream_id, stream_name, topic_name, post_id):
    '''
    https://example.zulipchat.com/#narrow/stream/213222-general/topic/hello/near/179892604
    '''
    sanitized = urllib.parse.quote(
        '{0}-{1}/topic/{2}/near/{3}'.format(stream_id, stream_name, topic_name, post_id))
    return zulip_url + '#narrow/stream/' + sanitized

def archive_stream_url(site_url, html_root, sanitized_stream_name):
    '''
    http://127.0.0.1:4000/archive/213222general/index.html
    '''
    path = f'{html_root}/{sanitized_stream_name}/index.html'
    return urllib.parse.urljoin(site_url, path)

def archive_topic_url(site_url, html_root, sanitized_stream_name, sanitized_topic_name):
    '''
    http://127.0.0.1:4000/archive/213222general/74282newstreams.html
    '''
    path = f'{html_root}/{sanitized_stream_name}/{sanitized_topic_name}.html'
    return urllib.parse.urljoin(site_url, path)

def archive_message_url(site_url, html_root, sanitized_stream_name, sanitized_topic_name, msg_id):
    base_url = urllib.parse.urljoin(site_url, html_root)
    full_url = f'{base_url}/{sanitized_stream_name}/{sanitized_topic_name}#{msg_id}'
    return full_url
