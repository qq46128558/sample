# dig

dig命令是常用的域名查询工具，可以用来测试域名系统工作是否正常。

## 语法

dig(选项)(参数)

## 选项

~~~
@<服务器地址>：指定进行域名解析的域名服务器；
-b<ip地址>：当主机具有多个IP地址，指定使用本机的哪个IP地址向域名服务器发送域名查询请求；
-f<文件名称>：指定dig以批处理的方式运行，指定的文件中保存着需要批处理查询的DNS任务信息；
-P：指定域名服务器所使用端口号；
-t<类型>：指定要查询的DNS数据类型；
-x<IP地址>：执行逆向域名查询；
-4：使用IPv4；
-6：使用IPv6；
-h：显示指令帮助信息。
+trace : 從.(root)開始追蹤
~~~

## 参数

~~~
主机：指定要查询域名主机；
查询类型：指定DNS查询的类型；
查询类：指定查询DNS的class；
查询选项：指定查询选项。
~~~

## 實例

### dns查詢流程

當你在瀏覽器的網址列輸地址，你的電腦就會依據相關設定 (在 Linux 底下就是利用 /etc/resolv.conf 這個檔案) 所提供的 DNS 的 IP 去進行連線查詢了

~~~
dig +trace www.dsclub.online

; <<>> DiG 9.10.3-P4-Ubuntu <<>> +trace www.dsclub.online
;; global options: +cmd
.                       128730  IN      NS      e.root-servers.net.
.                       128730  IN      NS      g.root-servers.net.
.                       128730  IN      NS      j.root-servers.net.
.                       128730  IN      NS      h.root-servers.net.
.                       128730  IN      NS      m.root-servers.net.
.                       128730  IN      NS      b.root-servers.net.
.                       128730  IN      NS      f.root-servers.net.
.                       128730  IN      NS      k.root-servers.net.
.                       128730  IN      NS      d.root-servers.net.
.                       128730  IN      NS      c.root-servers.net.
.                       128730  IN      NS      i.root-servers.net.
.                       128730  IN      NS      l.root-servers.net.
.                       128730  IN      NS      a.root-servers.net.
.                       128730  IN      RRSIG   NS 8 0 518400 20190123170000 20190110160000 16749 . mv7bGs2fMd6YYspyjjBaSobmnKm7QVm0aBrYl5FDuJOkuoIc6T2P4X2l mgwcMX6qAGtCTyxPx1Ovn741QX5UzbWm7s1Jc6NCDjOCB9X27wA8qtwD f4wRHS6e21YgNcY2P1INv2Rlz/DhcQF6rLsAMpO6yBVsQbUwVTW+6Ak1 N6UXmiER7/wxOrU/+AJ8StUK3He3y2qflHMH7wm6SdSNiINcu4sGy8Wc mbxRKS8MduWNd87jCbRYPQ0a9EIjiDc4HN2J8QxqyR2WkXLh/XA7x2TP hpFIlpBlRPx1vl5w+YvEEgEicxfjPyhMSunXBO746dRsvaoQ5FMKhPws pSgnzA==
;; Received 525 bytes from 100.100.2.136#53(100.100.2.136) in 0 ms

online.                 172800  IN      NS      a.nic.online.
online.                 172800  IN      NS      b.nic.online.
online.                 172800  IN      NS      c.nic.online.
online.                 172800  IN      NS      d.nic.online.
online.                 86400   IN      DS      4267 8 1 A038DA06A96AD8E9BFE2BA78C392FF7804B4CD2B
online.                 86400   IN      DS      4267 8 2 66D7010609CB19E99AD1DA2833DDAB8CA2E7ACC1CE870CC28D29E76E B53D39BA
online.                 86400   IN      RRSIG   DS 8 1 86400 20190128170000 20190115160000 16749 . cL+2Ll3h+4oGt1r+x2J7tETRb7h9a+ysEfxFuO+VITicEAOkMA4ul3Ou f58v7HVCec1XVwKm271MFeDfk34KmYerYNJxb0SC6Pq35SyOUI7qx1zp MGHFTr0Ep0jZ6JMk4HgbChpcwzZ7menZmgmmMx9z/MOscK//FgFkG3fo tgv6XbYQ5T5PpV4lEuDKz+uLaMCnA5x+7A0OkX+twa3lau4VDv1WtxCy dq9evJHciM7Tptrq8X6N1AeQeFM8L1DpKxoQUZqx2UfzxztzUQgSjXki 2aw6wH4quhpfzKdokGGPobvvkqHoehOIsCt6pTlQXCFXiGb7bflVi85f UVQxRQ==
;; Received 661 bytes from 192.5.5.241#53(f.root-servers.net) in 186 ms

dsclub.ONLINE.          3600    IN      NS      dns10.hichina.com.
dsclub.ONLINE.          3600    IN      NS      dns9.hichina.com.
6oebcchg2j40rs97rhg868u50oi7huk0.ONLINE. 3600 IN NSEC3 1 1 1 - 6OHSD4K91BGIJ9GGAPC1I5NANG5KPRNV NS SOA RRSIG DNSKEY NSEC3PARAM
6oebcchg2j40rs97rhg868u50oi7huk0.ONLINE. 3600 IN RRSIG NSEC3 8 2 3600 20190121021026 20181222053715 42813 online. oszdTwH4ivh2FIQXo7e/k6OXqjREP6KohibukOJHufYowppuA+dKV7sY ATsjjYHBpeRWQEp78CPK2wnj0eOWl4ldq551uXF1ciaqyIfNOGIH63mY jR05qzM8ZdSiAjvNtqoGcgsjwhrRPeZZ6g6Ceh/g7O4u0kf0UppguXiH vow=
3cvsvlr2lrmt1m8uig9ufd990c9n907t.ONLINE. 3600 IN NSEC3 1 1 1 - 3D48FMI9HRS6L7A68A9K45F8POEFKGE1 NS DS RRSIG
3cvsvlr2lrmt1m8uig9ufd990c9n907t.ONLINE. 3600 IN RRSIG NSEC3 8 2 3600 20190121041430 20181222085347 42813 online. pTQg6bC6+Fpe6MWe/iXNmUbaiayzg5++Xi0cEmlWRGd6uPH0WvqcKCWk IAMHl78yuMnBjY/74j4HgD9qQ/9spFhVV+zSejY3ZQ8CuVZUzcXY0F7f 3EfqZW7pbzAsh6XO3g6Bfw+NsKXFRYek6EzhtF6+vi+nCBQAxEksniYA akk=
;; Received 600 bytes from 185.38.99.7#53(c.nic.online) in 65 ms

www.dsclub.online.      600     IN      A       47.106.126.78
;; Received 62 bytes from 106.11.211.56#53(dns10.hichina.com) in 43 ms
~~~

(DNS)100.100.2.136>> 192.5.5.241#53(f.root-servers.net)>>185.38.99.7#53(c.nic.online)>>106.11.211.56#53(dns10.hichina.com)

>>www.dsclub.online.      600     IN      A       47.106.126.78

DNS 使用的是那一個 port 呢？那就是 53 這個 port 啦！你可以到你的 Linux 底下的 /etc/services 這個檔案看看！搜尋一下 domain 這個關鍵字，就可以查到 53 這個 port 啦！

### dig linux.vbird.org 

~~~
; <<>> DiG 9.10.3-P4-Ubuntu <<>> linux.vbird.org
;; global options: +cmd
;; Got answer:
;; ->>HEADER<<- opcode: QUERY, status: NOERROR, id: 54037
;; flags: qr rd ra; QUERY: 1, ANSWER: 1, AUTHORITY: 0, ADDITIONAL: 1

;; OPT PSEUDOSECTION:
; EDNS: version: 0, flags:; udp: 4096
;; QUESTION SECTION:
;linux.vbird.org.               IN      A

;; ANSWER SECTION:
linux.vbird.org.        600     IN      A       140.116.44.180

;; Query time: 175 msec
;; SERVER: 100.100.2.136#53(100.100.2.136)
;; WHEN: Thu Jan 17 01:30:05 CST 2019
;; MSG SIZE  rcvd: 60
~~~

QUESTION SECTION: 顯示所要查詢的內容

ANSWER SECTION: 依據剛剛的 QUESTION 去查詢所得到的結果

600: 就是允許查詢者能夠保留這筆記錄多久的意思 (快取)，在 linux.vbird.org 的設定中，預設可以保留 600 秒

## 常見的正解檔 RR(Resource Record) 相關資訊

~~~
[domain]    IN  [[RR type]  [RR data]]
主機名稱.   IN  A           IPv4 的 IP 位址
主機名稱.   IN  AAAA        IPv6 的 IP 位址
領域名稱.   IN  NS          管理這個領域名稱的伺服器主機名字.
領域名稱.   IN  SOA         管理這個領域名稱的七個重要參數(容後說明)
領域名稱.   IN  MX          順序數字  接收郵件的伺服器主機名字
主機別名.   IN  CNAME       實際代表這個主機別名的主機名字.
~~~

## SOA ：查詢管理領域名稱的伺服器管理資訊

	dig -t soa dsclub.online
~~~
;; ANSWER SECTION:
dsclub.online.          600     IN      SOA     dns9.hichina.com. hostmaster.hichina.com. 2018091409 3600 1200 86400 360

這七個參數的意義依序是：
Master DNS 伺服器主機名稱: dns9.hichina.com
管理員的 email: hostmaster@hichina.com
序號 (Serial)：這個序號代表的是這個資料庫檔案的新舊，序號越大代表越新。2018091409 : 2018/09/14第9次更新
更新頻率 (Refresh)：那麼啥時 slave 會去向 master 要求資料更新的判斷？ 就是這個數值定義的。3600 秒
失敗重新嘗試時間 (Retry)：如果因為某些因素，導致 slave 無法對 master 達成連線， 那麼在多久的時間內，slave 會嘗試重新連線到 master。 1200 秒
失效時間 (Expire)：如果一直失敗嘗試時間，持續連線到達這個設定值時限， 那麼 slave 將不再繼續嘗試連線，並且嘗試刪除這份下載的 zone file 資訊。86400 秒
快取時間 (Minumum TTL)：如果這個資料庫 zone file 中，每筆 RR 記錄都沒有寫到 TTL 快取時間的話，那麼就以這個 SOA 的設定值為主。 360 秒
~~~

~~~
# 其他限制
Refresh >= Retry *2
Refresh + Retry < Expire
Expire >= Rrtry * 10
Expire >= 7Days
~~~


## CNAME的作用

這個 CNAME 有啥好處呢？用 A 就好了吧？其實還是有好處的，舉例來說，如果你有一個 IP，這個 IP 是給很多主機名稱使用的。 那麼當你的 IP 更改時，所有的資料就得通通更新 A 標誌才行。如果你只有一個主要主機名稱設定 A，而其他的標誌使用 CNAME 時，那麼當 IP 更改，那你只要修訂一個 A 的標誌，其他的 CNAME 就跟著變動了！處理起來比較容易啊！

## MX ：查詢某領域名稱的郵件伺服器主機名稱

	dig -t mx google.com

~~~
;; ANSWER SECTION:
google.com.             600     IN      MX      40 alt3.aspmx.l.google.com.
google.com.             600     IN      MX      20 alt1.aspmx.l.google.com.
google.com.             600     IN      MX      50 alt4.aspmx.l.google.com.
google.com.             600     IN      MX      10 aspmx.l.google.com.
google.com.             600     IN      MX      30 alt2.aspmx.l.google.com.
~~~

RR Data前面的數值是？

由於擔心郵件會遺失，因此較大型的企業會有多部這樣的上層郵件伺服器來預先收受信件。 那麼到底哪部郵件主機會先收下呢？就以數字較小的那部優先囉！舉例來說，如果你去查 google.com 的 MX 標誌， 就會發現他有 5 部這樣的伺服器呢！

