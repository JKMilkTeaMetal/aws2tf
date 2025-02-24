import common
import boto3
import globals
import inspect

def get_aws_kinesis_firehose_delivery_stream(type, id, clfn, descfn, topkey, key, filterid):
    if globals.debug:
        print("--> In "+str(inspect.currentframe().f_code.co_name)+" doing " + type + ' with id ' + str(id) +
              " clfn="+clfn+" descfn="+descfn+" topkey="+topkey+" key="+key+" filterid="+filterid)
    try:
        response = []
        client = boto3.client(clfn)
        if id is None:
            response = client.list_delivery_streams()
            if response[topkey] == []: 
                print("Empty response for "+type+ " id="+str(id)+" returning"); return True
            for j in response[topkey]:
                # have the name - not must get the arn
                response = client.describe_delivery_stream(DeliveryStreamName=j)
                k=response['DeliveryStreamDescription']
                common.write_import(type,k[key],None) 
                pkey=type+"."+j
                globals.rproc[pkey]=True

        else:      
            response = client.describe_delivery_stream(DeliveryStreamName=id)
            if response == []: 
                print("Empty response for "+type+ " id="+str(id)+" returning")
                pkey=type+"."+id
                globals.rproc[pkey]=True
                return True
            j=response['DeliveryStreamDescription']
            common.write_import(type,j[key],None)
            pkey=type+"."+id
            globals.rproc[pkey]=True
            

    except Exception as e:
        common.handle_error(e,str(inspect.currentframe().f_code.co_name),clfn,descfn,topkey,id)

    return True