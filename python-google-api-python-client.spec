Name:		python-google-api-python-client
Version:	2.187.0
Release:	2
Source0:	https://files.pythonhosted.org/packages/source/g/google-api-python-client/google_api_python_client-%{version}.tar.gz
Summary:	Google API Client Library for Python
URL:		https://pypi.org/project/google-api-python-client/
License:	Apache 2.0
Group:		Development/Python
BuildSystem:	python
BuildArch:	noarch

%description
Google API Client Library for Python

%files
%{py_sitedir}/apiclient
%{py_sitedir}/googleapiclient
%{py_sitedir}/google_api_python_client-*.*-info
