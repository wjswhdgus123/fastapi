import requests
import json
import re

# AWX 설정
awx_url = 'http://awx.bestpath.co.kr/'
api_token = 'uvTnci5DidwRxI2pMNJrQZA0Ft9im5'
job_id = 56

# 특정 Job ID의 실행 결과 (stdout) 가져오기
def get_job_stdout(job_id):
    headers = {'Authorization': f'Bearer {api_token}'}
    url = f'{awx_url}api/v2/jobs/{job_id}/stdout/?format=json'

    response = requests.get(url, headers=headers)
    data = response.json()
    

    
    if response.status_code == 200:
        return data
    else:
        print(f'Failed to retrieve job stdout. Status code: {response.status_code}')
        return None
def remove_ansi_escape_sequences(text):
    ansi_escape = re.compile(r'\x1B(?:[@-Z\\-_]|\[[0-?]*[ -/]*[@-~])')
    return ansi_escape.sub('', text)

def pasing(text):
    patten = r'ok:\s\[.*\]\s=>\s{.*?\n.*\n.*\n.*\n}'
    #ipaptten = r'([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\.){3}([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])'
    ipaptten = r'(([1-9]?\d|1\d{2}|2([0-4]\d)|25[0-5])\.){3}([1-9]?\d|1\d{2}|2([0-4]\d)|25[0-5])'
    jobname = r'".*?":'
    resultpatten = r'\[\W.*"'
    lastresult = r'".*?"'

    
    result=re.finditer(patten,text)
    for m in result:
        mdata = m.group()
       
        ip=re.search(ipaptten,mdata).group()
        jobs=re.search(jobname,mdata).group()
        result=re.search(resultpatten,mdata).group()
        result2=re.search(lastresult,result).group()
        print(ip , jobs, result2)

        
        
    return
    






data = get_job_stdout(job_id)
data2 = data['content']
a = remove_ansi_escape_sequences(data2)
print(a)

