import common
import boto3
import globals
import inspect

def get_aws_dms_replication_instance(type, id, clfn, descfn, topkey, key, filterid):
    if globals.debug:
        print("--> In "+str(inspect.currentframe().f_code.co_name)+" doing " + type + ' with id ' + str(id) +
              " clfn="+clfn+" descfn="+descfn+" topkey="+topkey+" key="+key+" filterid="+filterid)
    try:
        response = []
        client = boto3.client(clfn)
        paginator = client.get_paginator(descfn)
        for page in paginator.paginate():
                response = response + page[topkey]
        print(str(response))
        if response == []: print("Empty response for "+type+ " id="+str(id)+" returning"); return True
        for j in response:
            if id is None:
                common.write_import(type,j[key],None) 
            else:
                if "arn:" in id:
                    if j['ReplicationInstanceArn']==id:
                        common.write_import(type,j[key],None) 

    except Exception as e:
        common.handle_error(e,str(inspect.currentframe().f_code.co_name),clfn,descfn,topkey,id)

    return True