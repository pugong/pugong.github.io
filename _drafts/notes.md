---
layout: post
title: notes
description: 
category: blog
---

[message queue](https://zhuanlan.zhihu.com/p/21649950)


postgres

change owner:

REASSIGN OWNED BY old_role [, ...] TO new_role
    
Note: As @trygvis mentions in the answer below, the REASSIGN OWNED command is available since at least version 8.2, and is a much easier method.

Since you're changing the ownership for all tables, you likely want views and sequences too. Here's what I did:

Tables:
for tbl in `psql -qAt -c "select tablename from pg_tables where schemaname = 'public';" prpv` ; do  psql -c "alter table \"$tbl\" owner to prpvopr" prpv ; done

Sequences:
for tbl in `psql -qAt -c "select sequence_name from information_schema.sequences where sequence_schema = 'public';" prpv` ; do  psql -c "alter table \"$tbl\" owner to prpvopr" prpv ; done

Views:
for tbl in `psql -qAt -c "select table_name from information_schema.views where table_schema = 'public';" prpv` ; do  psql -c "alter table \"$tbl\" owner to prpvopr" prpv ; done

You could probably DRY that up a bit since the alter statements are identical for all three.



## 距离需求

1. 获取上次位置
2. 获取上次时间 （redis ttl）
3. 计算和本次距离
4. 计算时速，比较时速

### 距离算法

```java
        /*
            The Haversine formula according to Dr. Math.
            http://mathforum.org/library/drmath/view/51879.html
                
            dlon = lon2 - lon1
            dlat = lat2 - lat1
            a = (sin(dlat/2))^2 + cos(lat1) * cos(lat2) * (sin(dlon/2))^2
            c = 2 * atan2(sqrt(a), sqrt(1-a)) 
            d = R * c
                
            Where
                * dlon is the change in longitude
                * dlat is the change in latitude
                * c is the great circle distance in Radians.
                * R is the radius of a spherical Earth.
                * The locations of the two points in 
                    spherical coordinates (longitude and 
                    latitude) are lon1,lat1 and lon2, lat2.
        */
        
        Double sourceLat, sourceLng, destlat, destlng, a, c, distance, dLat, dLng;
        double earthRadius = 6371; //km

        dLat=Math.toRadians(destlat-sourceLat);
        dLng=Math.toRadians(destlng-sourceLng);
        a = Math.sin(dLat/2) * Math.sin(dLat/2) +
                   Math.cos(Math.toRadians(myLocLat)) * Math.cos(Math.toRadians(lat)) *
                   Math.sin(dLng/2) * Math.sin(dLng/2);
        c = 2 * Math.atan2(Math.sqrt(a), Math.sqrt(1-a));
        distance = earthRadius * c;
```


## sequence id

1. uuid
2. hashid 不唯一
3. uuid hash 不唯一




## 签名算法

### MD5 
1. filter keys
2. sort keys
3. MD5 hashing

``` java

        // filter
        Map<String, String> validParams = new HashMap<>();

        for(Map.Entry<String, String> kv : signingParams.entrySet()){
            if (Strings.isNullOrEmpty(kv.getValue())
                    || SignFields.SIGN.field().equals(kv.getKey())
                    || SignFields.SIGN_TYPE.field().equals(kv.getKey())){
                continue;
            }
            validParams.put(kv.getKey(), kv.getValue());
        }

        
        // sort keys
        List<String> keys = new ArrayList<>(params.keySet());
        Collections.sort(keys);
        StringBuilder signString = new StringBuilder();
        for (int i = 0; i < keys.size(); i++) {
            String key = keys.get(i);
            String value = params.get(key);
            if (i == keys.size() - 1) {
                //拼接时，不包括最后一个&字符
                signString.append(key).append("=").append(value);
            } else {
                signString.append(key).append("=").append(value).append("&");
            }
        }
        return signString.toString();    


        // md5 sign
        String md5String = signString + key
        byte[] digest = MessageDigest.getInstance("MD5").digest(md5String.getBytes(CHARSET));
        return hex(digest);

```


