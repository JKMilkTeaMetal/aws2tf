import common
import boto3
import globals
import inspect

def get_aws_ram_resource_share(type, id, clfn, descfn, topkey, key, filterid):
    if globals.debug:
        print("--> In "+str(inspect.currentframe().f_code.co_name)+" doing " + type + ' with id ' + str(id) +
              " clfn="+clfn+" descfn="+descfn+" topkey="+topkey+" key="+key+" filterid="+filterid)
    try:
        response = []
        client = boto3.client(clfn)
        if id is None:
            paginator = client.get_paginator(descfn)
            for page in paginator.paginate(resourceOwner='SELF'):
                response = response + page[topkey]
            if response == []: print("Empty response for "+type+ " id="+str(id)+" returning"); return True
            for j in response:
                common.write_import(type,j[key],None) 
                common.add_dependancy("aws_ram_principal_association",j[key])

        else:      
            response = client.get_resource_shares(resourceOwner='SELF')
            if response['resourceShares'] == []: print("Empty response for "+type+ " id="+str(id)+" returning"); return True
            for j in response['resourceShares']:
                common.write_import(type,j['resourceShareArn'],None)
                common.add_dependancy("aws_ram_principal_association",j['resourceShareArn'])

    except Exception as e:
        common.handle_error(e,str(inspect.currentframe().f_code.co_name),clfn,descfn,topkey,id)

    return True

# aws_ram_principal_association #
def get_aws_ram_principal_association(type, id, clfn, descfn, topkey, key, filterid):
    if globals.debug:
        print("--> In "+str(inspect.currentframe().f_code.co_name)+" doing " + type + ' with id ' + str(id) +
              " clfn="+clfn+" descfn="+descfn+" topkey="+topkey+" key="+key+" filterid="+filterid)
    try:
        response = []
        client = boto3.client(clfn)
        if id is None:
            paginator = client.get_paginator(descfn)
            for page in paginator.paginate(resourceOwner='SELF'):
                response = response + page[topkey]
            if response == []: print("Empty response for "+type+ " id="+str(id)+" returning"); return True
            for j in response:
                pkey=j['resourceShareArn']+","+j[key]
                common.write_import(type, pkey, None)
                pkey=type+"."+j['resourceShareArn']
                globals.rproc[pkey]=True

        else:
            if id.startswith("arn:"):
                response = client.list_principals(resourceOwner='SELF',resourceShareArns=[id])
                if response[topkey] == []: print("Empty response for "+type+ " id="+str(id)+" returning"); return True
                for j in response[topkey]:
                    pkey=j['resourceShareArn']+","+j[key]
                    common.write_import(type, pkey, None)
                    pkey=type+"."+id
                    globals.rproc[pkey]=True

    except Exception as e:
        common.handle_error(e, str(inspect.currentframe().f_code.co_name), clfn, descfn, topkey, id)

    return True