Not working yet.
Need to figure out how wv_proto2_pb2.py works, then change the mechanism for generating a license request.
It looks like wv_proto2.proto contains description of this mechanism.
<h3>First run: </h3>
Copy headers and cookies of POST license request from browser to headers.py and cookies.py respectively like dictionaries.  
</br>

```
pip install -r requirements.txt # if doesn't work try pip3
py l3.py
Input MPD URL: https://strm.yandex.ru/vh-ottenc-converted/vod-content/.../.../dash-cenc/sdr_uhd_hevc_ec3.mpd
```
