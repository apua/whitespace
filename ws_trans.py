'''
Goal:
  usage: CMD -f [] -m [] [] []
  purpose: download file / trans pure / trans lexical tokens

version: 0.1
'''

def translate_content(content, orig_token, to_token):
  return content.translate(str.maketrans(orig_token,to_token))

def get_content(path):
  if path.startswith('http://'):
    from urllib.request import urlopen
    return urlopen(path).read().decode('UTF8')
  else:
    return open(path).read()

def clean_content(content, lexical_token=' \t\n'):
  return ''.join(c for c in content if c in lexical_token)

def output_result(content, output_file=None):
  if output_file:
    with open(output_file,'w') as f:
      f.write(content)
  else:
    print(content)

if __name__=='__main__':
  path = "http://compsoc.dur.ac.uk/whitespace/tutorial.html"
  C = get_content(path)
  C = clean_content(C)
  C = translate_content(C,' \t\n', 'STL')
  output_result(C,'factorial')
