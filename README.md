Works only if the site does not require specific json-formatted data in the license request. 
And if it requires and you want to add its support, write to issues specifying the required json-formatted fields and the algorithm for their formation (if not static).

Further about kinonpoisk (hello to compatriots):</br>
Not working yet.
It is necessary to find out how the POST request is signed (the signature field in the request payload). 
It looks like a simple hash of sha1, but from the looks of it, this is not it, but the Amazon's AWS Signature Version 4. Or I am doing something wrong and everything is much easier...
Any ideas are appreciated, write to issues.

[Parsed payload of license request](https://user-images.githubusercontent.com/43696206/145263764-349dd8be-58ec-4d42-9524-4a098b0fe5e3.png)

<h3>First run: </h3>
Copy headers (with cookies) of POST license request from browser to headers.py like dictionary.
</br>

```
pip install -r requirements.txt # if doesn't work try pip3
py l3.py
Input MPD URL: https://strm.yandex.ru/vh-ottenc-converted/vod-content/.../.../dash-cenc/sdr_uhd_hevc_ec3.mpd
```
