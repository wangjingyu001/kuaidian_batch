import time
import redis
import schedule
import csv

rd = redis.Redis('127.0.0.1', 6379, db=0, decode_responses=True)
import requests
import execjs


def get_sign(e):
    jscode = """


function x1(e){
function l(e) {
                var t, i = [];
                for (t in e) {
                    i.push([t, e[t]]);
                }
                return d(i, function(e, t) {
                    return e[0] > t[0];
                }),
                i;
            }
           function d(e, t) {
                for (var i = 0; i < e.length - 1; i++) {
                    for (var a, r = !0, n = 0; n < e.length - 1 - i; n++) {
                        0 < t(e[n], e[n + 1]) && (a = e[n],
                        e[n] = e[n + 1],
                        e[n + 1] = a,
                        r = !1);
                    }
                    if (r)
                        return !1;
                }
            };
function u(e) {
                for (var t = l(e), i = "", a = 0; a < t.length; a++) {
                    i += t[a][0] + "" + t[a][1];
                }
                return "15cdf1eaf2110a3009bf2be5d3e53c3c"+i+"15cdf1eaf2110a3009bf2be5d3e53c3c"
            }
return u(e)
}

function x2(e){

function g(e) {
                return unescape(encodeURIComponent(e));
            }
function d(e) {
                var t = [];
                for (t[(e.length >> 2) - 1] = void 0,
                a = 0; a < t.length; a += 1) {
                    t[a] = 0;
                }
                for (var i = 8 * e.length, a = 0; a < i; a += 8) {
                    t[a >> 5] |= (255 & e.charCodeAt(a / 8)) << a % 32;
                }
                return t;
            }

function a(e, t) {
                var i = (65535 & e) + (65535 & t);
                return (e >> 16) + (t >> 16) + (i >> 16) << 16 | 65535 & i;
            }
            function r(e, t, i, r, n, s) {
                return a((s = a(a(t, e), a(r, s))) << n | s >>> 32 - n, i);
            }
            function n(e, t, i, a, n, s, o) {
                return r(t & i | ~t & a, e, t, n, s, o);
            }
            function s(e, t, i, a, n, s, o) {
                return r(t & a | i & ~a, e, t, n, s, o);
            }
            function o(e, t, i, a, n, s, o) {
                return r(t ^ i ^ a, e, t, n, s, o);
            }
            function c(e, t, i, a, n, s, o) {
                return r(i ^ (t | ~a), e, t, n, s, o);
            }
            function u(e, t) {
                var i, r, u, l;
                e[t >> 5] |= 128 << t % 32,
                e[14 + (t + 64 >>> 9 << 4)] = t;
                for (var d = 1732584193, A = -271733879, g = -1732584194, h = 271733878, f = 0; f < e.length; f += 16) {
                    A = c(A = c(A = c(A = c(A = o(A = o(A = o(A = o(A = s(A = s(A = s(A = s(A = n(A = n(A = n(A = n(r = A, g = n(u = g, h = n(l = h, d = n(i = d, A, g, h, e[f], 7, -680876936), A, g, e[f + 1], 12, -389564586), d, A, e[f + 2], 17, 606105819), h, d, e[f + 3], 22, -1044525330), g = n(g, h = n(h, d = n(d, A, g, h, e[f + 4], 7, -176418897), A, g, e[f + 5], 12, 1200080426), d, A, e[f + 6], 17, -1473231341), h, d, e[f + 7], 22, -45705983), g = n(g, h = n(h, d = n(d, A, g, h, e[f + 8], 7, 1770035416), A, g, e[f + 9], 12, -1958414417), d, A, e[f + 10], 17, -42063), h, d, e[f + 11], 22, -1990404162), g = n(g, h = n(h, d = n(d, A, g, h, e[f + 12], 7, 1804603682), A, g, e[f + 13], 12, -40341101), d, A, e[f + 14], 17, -1502002290), h, d, e[f + 15], 22, 1236535329), g = s(g, h = s(h, d = s(d, A, g, h, e[f + 1], 5, -165796510), A, g, e[f + 6], 9, -1069501632), d, A, e[f + 11], 14, 643717713), h, d, e[f], 20, -373897302), g = s(g, h = s(h, d = s(d, A, g, h, e[f + 5], 5, -701558691), A, g, e[f + 10], 9, 38016083), d, A, e[f + 15], 14, -660478335), h, d, e[f + 4], 20, -405537848), g = s(g, h = s(h, d = s(d, A, g, h, e[f + 9], 5, 568446438), A, g, e[f + 14], 9, -1019803690), d, A, e[f + 3], 14, -187363961), h, d, e[f + 8], 20, 1163531501), g = s(g, h = s(h, d = s(d, A, g, h, e[f + 13], 5, -1444681467), A, g, e[f + 2], 9, -51403784), d, A, e[f + 7], 14, 1735328473), h, d, e[f + 12], 20, -1926607734), g = o(g, h = o(h, d = o(d, A, g, h, e[f + 5], 4, -378558), A, g, e[f + 8], 11, -2022574463), d, A, e[f + 11], 16, 1839030562), h, d, e[f + 14], 23, -35309556), g = o(g, h = o(h, d = o(d, A, g, h, e[f + 1], 4, -1530992060), A, g, e[f + 4], 11, 1272893353), d, A, e[f + 7], 16, -155497632), h, d, e[f + 10], 23, -1094730640), g = o(g, h = o(h, d = o(d, A, g, h, e[f + 13], 4, 681279174), A, g, e[f], 11, -358537222), d, A, e[f + 3], 16, -722521979), h, d, e[f + 6], 23, 76029189), g = o(g, h = o(h, d = o(d, A, g, h, e[f + 9], 4, -640364487), A, g, e[f + 12], 11, -421815835), d, A, e[f + 15], 16, 530742520), h, d, e[f + 2], 23, -995338651), g = c(g, h = c(h, d = c(d, A, g, h, e[f], 6, -198630844), A, g, e[f + 7], 10, 1126891415), d, A, e[f + 14], 15, -1416354905), h, d, e[f + 5], 21, -57434055), g = c(g, h = c(h, d = c(d, A, g, h, e[f + 12], 6, 1700485571), A, g, e[f + 3], 10, -1894986606), d, A, e[f + 10], 15, -1051523), h, d, e[f + 1], 21, -2054922799), g = c(g, h = c(h, d = c(d, A, g, h, e[f + 8], 6, 1873313359), A, g, e[f + 15], 10, -30611744), d, A, e[f + 6], 15, -1560198380), h, d, e[f + 13], 21, 1309151649), g = c(g, h = c(h, d = c(d, A, g, h, e[f + 4], 6, -145523070), A, g, e[f + 11], 10, -1120210379), d, A, e[f + 2], 15, 718787259), h, d, e[f + 9], 21, -343485551),
                    d = a(d, i),
                    A = a(A, r),
                    g = a(g, u),
                    h = a(h, l);
                }
                return [d, A, g, h];
            }
            function l(e) {
                for (var t = "", i = 32 * e.length, a = 0; a < i; a += 8) {
                    t += String.fromCharCode(e[a >> 5] >>> a % 32 & 255);
                }
                return t;
            }

function h(e) {
                return l(u(d(e = g(e)), 8 * e.length));
            }

            function A(e) {
                for (var t, i = "0123456789abcdef", a = "", r = 0; r < e.length; r += 1) {
                    t = e.charCodeAt(r),
                    a += i.charAt(t >>> 4 & 15) + i.charAt(15 & t);
                }
                return a;
            }
return A(h(e))
}
function x3(e){
return x2(x1(e))
}
    """
    # e = {"pageIndex": 3,
    #      "pageSize": 10,
    #      "userLatStr": 40.22077,
    #      "userLngStr": 116.23128,
    #      "distance": "",
    #      "chargeType": 1,
    #      "tagId": -1,
    #      "tagIds": "",
    #      "searchType": 2,
    #
    #      "destLngStr": 116.313299,
    #      "destLatStr": 40.010379,
    #
    #      "token": "",
    #      "app_key": "kd_prod_mp",
    #      "timestamp": 1631637370040,
    #      "app_terminal": "mp",
    #      "latitude": 40.22077,
    #      "longitude": 116.23128,
    #      "perm_id": "963E412C221941C09B1F452AD5C0333E"}
    jsload = execjs.compile(jscode)
    result = jsload.call('x3', e)
    # print(result)
    return result


# get_sign(1)
def get_data(title0, destLngStr, destLatStr):
    url = 'https://mpcs.fleetingpower.com/services/v3/charge/v3/stationInfoListWithPageNew'
    for page in range(1, 50):
        timestamp = int(time.time() * 1000)
        form_data = {"pageIndex": page,
                     "pageSize": 10,
                     "userLatStr": 40.22077,
                     "userLngStr": 116.23128,
                     "distance": "",
                     "chargeType": 1,
                     "tagId": -1,
                     "tagIds": "",
                     "searchType": 2,

                     "destLngStr": destLngStr,
                     "destLatStr": destLatStr,

                     "token": "",
                     "app_key": "kd_prod_mp",
                     "timestamp": timestamp,
                     "app_terminal": "mp",
                     "latitude": 40.22077,
                     "longitude": 116.23128,
                     "perm_id": "963E412C221941C09B1F452AD5C0333E"
                     }
        sign = get_sign(form_data)
        form_data['sign'] = sign
        # print(form_data)
        r = requests.post(url, data=form_data, verify=False)
        # print(r.json())
        data_list = r.json()['result']['chargeStationInfoList']
        if not data_list:
            break
        print(data_list)
        # input('stop')
        for item in data_list:
            title = item['czbStationName']
            czbOperatorName = item['czbOperatorName']
            kuai = item['directRemark']
            kuai_last = kuai.split('/')[0]
            kuai_all = kuai.split('/')[1]
            man = item['alternateRemark']
            man_last = man.split('/')[0]
            man_all = man.split('/')[1]
            address = item['address']
            yuanjia = item['originalPrice']
            xianjia =  item['memberPrice']
            zhekou = item['hasReducedPrice']
            if not zhekou:
                zhekou='0'
            print(title0, title, kuai, man)
            rd.sadd('快电数据', '&'.join([title0, title, address, kuai_last, kuai_all, man_last, man_all,yuanjia,xianjia,zhekou,czbOperatorName]))
            # writer.writerow(['采集点&位置&具体位置&快充剩余&快充总量&慢充剩余&慢充总量&原价&现价&折扣'])
        # input('stop')


def get_location():
    # rd.
    # https://apis.map.qq.com/ws/place/v1/suggestion?keyword=%E9%95%BF%E6%98%A5%E5%B8%82&region=%E5%85%A8%E5%9B%BD&region_fix=0&policy=0&page_size=10&page_index=1&get_subpois=0&output=json&key=GTPBZ-PLDR5-7C6IC-Q3PNE-2IEA3-ILBGB&location=40.22077%2C116.23128
    url = "https://apis.map.qq.com/ws/place/v1/suggestion?keyword=%E9%95%BF%E6%98%A5%E5%B8%82&region=%E5%85%A8%E5%9B%BD&region_fix=0&policy=0&page_size=10&page_index=1&get_subpois=0&output=json&key=GTPBZ-PLDR5-7C6IC-Q3PNE-2IEA3-ILBGB&location=40.22077%2C116.23128"

    r = requests.get(url, verify=False)
    data_list = r.json()['data']
    print(data_list)

    for item in data_list:
        title = item['title']
        location = item['location']
        destLatStr = location['lat']
        destLngStr = location['lng']
        # print(title,location)
        get_data(title, destLngStr, destLatStr)
    get_csv()


def get_csv():
    data = rd.smembers('快电数据')
    with open(f'data{int(time.time())}.csv', 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow('采集点&位置&具体位置&快充剩余&快充总量&慢充剩余&慢充总量&原价&现价&折扣&充电站厂家'.split('&'))
        for item in data:
            writer.writerow(item.split('&'))
            rd.srem('快电数据', item)
    with open(f'{int(time.time())}', 'w') as f:
        pass

get_location()
schedule.every().hour.do(get_location)

while 1:
    schedule.run_pending()
    time.sleep(1)