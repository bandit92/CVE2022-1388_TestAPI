from fastapi import FastAPI, Request, HTTPException
from  subprocess  import run, PIPE, STDOUT 

app = FastAPI()

@app.post("/mgmt/tm/util/bash")
async def do_exec(request: Request):
    try:
        data = await request.json()
        print(data)
        if data['command'] == "run":
            utilCmdArgs = data['utilCmdArgs'].split(" ")
            args = ["bash"] + utilCmdArgs
            process = run(args,stdout=PIPE,stderr=STDOUT,text=True,errors="ignore")
            resp = process.stdout
            print(resp)
            return {
                "kind" : "tm:util:bash:runstat",
                "command": data['command'],
                "utilCmdArgs": data['utilCmdArgs'],
                "commandResult": resp
            }
    except Exception as e:
        raise HTTPException(status_code=404, detail="An Error Occurred")
