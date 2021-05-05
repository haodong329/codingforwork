import requests
import pytest
import xlrd
import json


def getfiledata(filename, sheetname):
    file = xlrd.open_workbook(filename)
    table = file.sheet_by_name(sheetname)
    reqheader = []
    reqparam = []
    for i in range(table.nrows-1):
        reqheader.append(table.row_values(i+1)[3])
        reqparam.append(table.row_values(i+1)[4])
    return reqparam


@pytest.mark.parametrize('reqparam', getfiledata('f:/teachApi.xls', 'course'))
def test_addcourse(reqparam):
    host = 'http://127.0.0.1:80'
    api_url = f'{host}/api/mgr/sq_mgr/'
    resp = requests.post(api_url, data=eval(reqparam))
    # resp.encoding = 'unicode_escape'
    print(resp.text)


if __name__ == '__main__':
    # getfiledata('f:/teachApi.xls', 'course')
    pytest.main()











