import common
def aws_datazone_domain(t1,tt1,tt2,flag1,flag2):
	skip=0
	return skip,t1,flag1,flag2

def aws_datazone_project(t1,tt1,tt2,flag1,flag2):
	skip=0
	return skip,t1,flag1,flag2

def aws_datazone_glossary(t1,tt1,tt2,flag1,flag2):
	skip=0
	return skip,t1,flag1,flag2

def aws_datazone_environment_blueprint_configuration(t1,tt1,tt2,flag1,flag2):
	skip=0
	return skip,t1,flag1,flag2

def aws_datazone_environment_profile(t1,tt1,tt2,flag1,flag2):
	skip=0
	if tt1=="domain_identifier" and tt2!="null":
		t1=tt1+" = aws_datazone_domain."+tt2+".id\n"
		common.add_dependancy("aws_datazone_domain",tt2)

	return skip,t1,flag1,flag2