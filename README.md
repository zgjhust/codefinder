# codefinder
A sina SAE app used to query the explanation of mvs(db2,cics) messages and codes.
## Installation
1. Download related IBM redbook to directory _original_, convert pdf to txt format and make some changes.
2. Convert the redbooks to json format,run the following script:
    `scripts/format_all.sh`
3. Install dependent python package:
    `pip install -r requirements.txt`
4. Deploy the project to sae.Refer to the [sae official site](http://www.sinacloud.com/doc/sae/python/index.html)for details about deploying apps.
5. Refer to [weixin official site](https://mp.weixin.qq.com) for details about how to configure weixin public account to send & recieve text messages to & from user defined http web app.

