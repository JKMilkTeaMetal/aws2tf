import common
import fixtf
import globals

def aws_eks_addon(t1,tt1,tt2,flag1,flag2):
    skip=0
    if tt1 == "cluster_name":
        t1=tt1 + " = aws_eks_cluster." + tt2 + ".id\n"
        common.add_dependancy("aws_eks_cluster",tt2)
    elif tt1 == "service_account_role_arn":
        if ":role/" in tt2:
            tt2=tt2.split("/")[-1]
            t1=tt1 + " = aws_iam_role." + tt2 + ".arn\n"
            common.add_dependancy("aws_iam_role",tt2)

    return skip,t1,flag1,flag2 


def aws_eks_cluster_auth(t1,tt1,tt2,flag1,flag2):
    skip=0
    if tt1 == "cluster_name":
        t1=tt1 + " = aws_eks_cluster." + tt2 + ".id\n"
        common.add_dependancy("aws_eks_cluster",tt2)

    return skip,t1,flag1,flag2

def aws_eks_pod_identity_association(t1,tt1,tt2,flag1,flag2):
    skip=0
    if tt1 == "cluster_name":
        t1=tt1 + " = aws_eks_cluster." + tt2 + ".id\n"
        common.add_dependancy("aws_eks_cluster",tt2)
    return skip,t1,flag1,flag2

def aws_eks_cluster(t1,tt1,tt2,flag1,flag2):
    skip=0
    ##if tt1 == "subnet_ids":  t1,skip = fixtf.deref_array(t1,tt1,tt2,"aws_subnet","subnet-",skip)
    ##elif tt1 == "security_group_ids": t1,skip = fixtf.deref_array(t1,tt1,tt2,"aws_security_group","sg-",skip)
    #if tt1 == "role_name":
    #    
    #    t1=tt1 + " = aws_iam_role." + tt2 + ".id\n"
    #    common.add_dependancy("aws_iam_role",tt2)
#    elif tt1 == "role_arn":
#        
#        if ":" in tt2: tt2=tt2.split("/")[-1]
#        t1=tt1 + " = aws_iam_role." + tt2 + ".arn\n"
#        common.add_dependancy("aws_iam_role",tt2)
    if tt1 == "key_arn":
        if ":" in tt2: tt2="k-"+tt2.split("/")[-1]
        t1=tt1 + " = aws_kms_key." + tt2 + ".arn\n"
        common.add_dependancy("aws_kms_key",tt2)
    elif tt1 == "version" and tt2=="jsonencode(1.3)": 
        print("******* aws_eks_cluster version 1.3",t1)
        t1=tt1 + " = \"1.30\"\n"
    return skip,t1,flag1,flag2


def aws_eks_fargate_profile(t1,tt1,tt2,flag1,flag2):
    skip=0
    ##if tt1 == "subnet_ids":  t1,skip = fixtf.deref_array(t1,tt1,tt2,"aws_subnet","subnet-",skip)
    if tt1 == "pod_execution_role_arn":     
        if ":" in tt2: tt2=tt2.split("/")[-1]
        if tt2 in globals.rolelist:
            t1=tt1 + " = aws_iam_role." + tt2 + ".arn\n"
            common.add_dependancy("aws_iam_role",tt2)
    elif tt1 == "cluster_name":
        t1=tt1 + " = aws_eks_cluster." + tt2 + ".id\n"
        common.add_dependancy("aws_eks_cluster",tt2)
    
    return skip,t1,flag1,flag2

def aws_eks_node_group(t1,tt1,tt2,flag1,flag2):
    skip=0
    if "launch_template {" in t1: 
        #print("******* flag1 true launch_template")
        flag1=True


    if "max_unavailable_percentage" in tt1:
        
        #print(tt1+" "+tt2)
        if tt2 == "0": skip=1

    elif "max_unavailable" in tt1:
        
        #print(tt1+" "+tt2)
        if tt2 == "0": skip=1

    elif "node_group_name_prefix" in tt1: skip=1
    elif tt1 == "cluster_name":
        t1=tt1 + " = aws_eks_cluster." + tt2 + ".id\n"
        common.add_dependancy("aws_eks_cluster",tt2)
    ##elif tt1 == "subnet_ids":  t1,skip = fixtf.deref_array(t1,tt1,tt2,"aws_subnet","subnet-",skip)
    elif tt1 == "node_role_arn":
        
        if ":" in tt2: tt2=tt2.split("/")[-1]
        t1=tt1 + " = aws_iam_role." + tt2 + ".arn\n"
        common.add_dependancy("aws_iam_role",tt2)
    elif tt1=="id":
        if tt2.startswith("lt-"):
            if flag1 is True:
                t1 = tt1 +" = aws_launch_template."+tt2+".id\n"
                common.add_dependancy("aws_launch_template",tt2)
                flag1=False
    
    elif tt1 == "name":
        if flag1 is True: 
            #print("----********"+tt2)
            t1=tt1 + " = aws_launch_template." + tt2 + ".name\n"
            common.add_dependancy("aws_launch_template",tt2)
            flag1=False
        else:
            skip=1
        
    
    return skip,t1,flag1,flag2


def aws_eks_identity_provider_config(t1, tt1, tt2, flag1, flag2):
    skip=0
    if tt1 == "cluster_name":
        t1=tt1 + " = aws_eks_cluster." + tt2 + ".id\n"
        common.add_dependancy("aws_eks_cluster",tt2)
    return skip,t1,flag1,flag2

def aws_eks_access_entry(t1, tt1, tt2, flag1, flag2):
    skip=0
    if tt1 == "cluster_name":
        t1=tt1 + " = aws_eks_cluster." + tt2 + ".id\n"
        common.add_dependancy("aws_eks_cluster",tt2)
    return skip,t1,flag1,flag2


def aws_eks_access_policy_association(t1, tt1, tt2, flag1, flag2):
    skip=0
    if tt1 == "cluster_name":
        t1=tt1 + " = aws_eks_cluster." + tt2 + ".id\n"
        common.add_dependancy("aws_eks_cluster",tt2)
    return skip,t1,flag1,flag2




