from concurrent.futures import ThreadPoolExecutor as Executor

urls = """google twitter facebook youtube pinterest tumblr
instagram reddit flickr meetup classmates microsoft apple
linkedin xing renren disqus snapchat twoo""".split()

""" twitter facebook youtube pinterest tumblr
instagram reddit flickr meetup classmates microsoft apple
linkedin xing renren disqus snapchat twoo whatsapp """

def fetch(url: str):
  from urllib import request, error
  try:
    data = request.urlopen(url).read()
    return f'{url}: length {len(data)}'
  except error.HTTPError as e:
    return f'{url}: {e}'

with Executor(max_workers=4) as exe:
  template = 'http://www.{}.com'
  jobs = [exe.submit(fetch, template.format(u)) for u in urls]
  results = [job.result() for job in jobs]

""" for u in urls:
  try:
    result = fetch(f'http://{u}.com')
    print(result)
  except error:
    print(error) """

print('\n'.join(results))