import threading
from time import sleep
import requests,re,random
from urllib.parse import parse_qs

class TweetsScraper:

    lop_time=0
    loping_limite=3
    search_data=[]
    data_profile=[]
    cookies_file =[{"cookes":"personalization_id='v1_dHHFLDyKtDVCMB311mOTGg==';lang=en;att=1-ycHI63cHXIvpuNVQFPl14HlqS4C7HiyLnKgrPAFU;auth_token=ba499e9788c9ba4d7bd5a22fd24327f5058da2d4;ct0=b86fb5f0515528aca84644829cdf3b9aa58e505e3000b1755d2f8c2e0453746521219ba508d27f8840470811f8b73485b983a7430df1e572cc35d9a8d0aa068923bc4a992b9509bae1d2668494af3a06;gt=1750018407460897212;_ga=GA1.2.1402762415.1706071873;kdt=oddzwALPLG4FY7nHIjRSrRt5qEXIEbT72YjAPBXg;_gid=GA1.2.678308757.1706071873;twid=u%3D1745514902863929344;guest_id=v1%3A170607187673692322;guest_id_ads=v1%3A170607187673692322;_twitter_sess=BAh7CSIKZmxhc2hJQzonQWN0aW9uQ29udHJvbGxlcjo6Rmxhc2g6OkZsYXNo%250ASGFzaHsABjoKQHVzZWR7ADoPY3JlYXRlZF9hdGwrCDL1zjmNAToMY3NyZl9p%250AZCIlZWI0NDFjNzBkMjgzMWE0ZTFiZDU5MTU1ZTE0ZDA2ZDE6B2lkIiU3Zjdh%250AYTFkYzJiMDQ4YWJlZDhlMzYyMTE5ZGI0YWJlYg%253D%253D--11a182538497f43357f1bdfbbd59fac05bc17db1;guest_id_marketing=v1%3A170607187673692322"},
{"cookes":"personalization_id='v1_dHHFLDyKtDVCMB311mOTGg==';lang=en;att=1-ycHI63cHXIvpuNVQFPl14HlqS4C7HiyLnKgrPAFU;auth_token=ba499e9788c9ba4d7bd5a22fd24327f5058da2d4;ct0=b86fb5f0515528aca84644829cdf3b9aa58e505e3000b1755d2f8c2e0453746521219ba508d27f8840470811f8b73485b983a7430df1e572cc35d9a8d0aa068923bc4a992b9509bae1d2668494af3a06;gt=1750018407460897212;_ga=GA1.2.1402762415.1706071873;kdt=oddzwALPLG4FY7nHIjRSrRt5qEXIEbT72YjAPBXg;_gid=GA1.2.678308757.1706071873;twid=u%3D1745514902863929344;guest_id=v1%3A170607187673692322;guest_id_ads=v1%3A170607187673692322;_twitter_sess=BAh7CSIKZmxhc2hJQzonQWN0aW9uQ29udHJvbGxlcjo6Rmxhc2g6OkZsYXNo%250ASGFzaHsABjoKQHVzZWR7ADoPY3JlYXRlZF9hdGwrCDL1zjmNAToMY3NyZl9p%250AZCIlZWI0NDFjNzBkMjgzMWE0ZTFiZDU5MTU1ZTE0ZDA2ZDE6B2lkIiU3Zjdh%250AYTFkYzJiMDQ4YWJlZDhlMzYyMTE5ZGI0YWJlYg%253D%253D--11a182538497f43357f1bdfbbd59fac05bc17db1;guest_id_marketing=v1%3A170607187673692322"},
{"cookes":"personalization_id='v1_dHHFLDyKtDVCMB311mOTGg==';lang=en;att=1-ycHI63cHXIvpuNVQFPl14HlqS4C7HiyLnKgrPAFU;auth_token=ba499e9788c9ba4d7bd5a22fd24327f5058da2d4;ct0=b86fb5f0515528aca84644829cdf3b9aa58e505e3000b1755d2f8c2e0453746521219ba508d27f8840470811f8b73485b983a7430df1e572cc35d9a8d0aa068923bc4a992b9509bae1d2668494af3a06;gt=1750018407460897212;_ga=GA1.2.1402762415.1706071873;kdt=oddzwALPLG4FY7nHIjRSrRt5qEXIEbT72YjAPBXg;_gid=GA1.2.678308757.1706071873;twid=u%3D1745514902863929344;guest_id=v1%3A170607187673692322;guest_id_ads=v1%3A170607187673692322;_twitter_sess=BAh7CSIKZmxhc2hJQzonQWN0aW9uQ29udHJvbGxlcjo6Rmxhc2g6OkZsYXNo%250ASGFzaHsABjoKQHVzZWR7ADoPY3JlYXRlZF9hdGwrCDL1zjmNAToMY3NyZl9p%250AZCIlZWI0NDFjNzBkMjgzMWE0ZTFiZDU5MTU1ZTE0ZDA2ZDE6B2lkIiU3Zjdh%250AYTFkYzJiMDQ4YWJlZDhlMzYyMTE5ZGI0YWJlYg%253D%253D--11a182538497f43357f1bdfbbd59fac05bc17db1;guest_id_marketing=v1%3A170607187673692322"},
{"cookes":"personalization_id='v1_dHHFLDyKtDVCMB311mOTGg==';lang=en;att=1-ycHI63cHXIvpuNVQFPl14HlqS4C7HiyLnKgrPAFU;auth_token=ba499e9788c9ba4d7bd5a22fd24327f5058da2d4;ct0=b86fb5f0515528aca84644829cdf3b9aa58e505e3000b1755d2f8c2e0453746521219ba508d27f8840470811f8b73485b983a7430df1e572cc35d9a8d0aa068923bc4a992b9509bae1d2668494af3a06;gt=1750018407460897212;_ga=GA1.2.1402762415.1706071873;kdt=oddzwALPLG4FY7nHIjRSrRt5qEXIEbT72YjAPBXg;_gid=GA1.2.678308757.1706071873;twid=u%3D1745514902863929344;guest_id=v1%3A170607187673692322;guest_id_ads=v1%3A170607187673692322;_twitter_sess=BAh7CSIKZmxhc2hJQzonQWN0aW9uQ29udHJvbGxlcjo6Rmxhc2g6OkZsYXNo%250ASGFzaHsABjoKQHVzZWR7ADoPY3JlYXRlZF9hdGwrCDL1zjmNAToMY3NyZl9p%250AZCIlZWI0NDFjNzBkMjgzMWE0ZTFiZDU5MTU1ZTE0ZDA2ZDE6B2lkIiU3Zjdh%250AYTFkYzJiMDQ4YWJlZDhlMzYyMTE5ZGI0YWJlYg%253D%253D--11a182538497f43357f1bdfbbd59fac05bc17db1;guest_id_marketing=v1%3A170607187673692322"},
{"cookes":"personalization_id='v1_dHHFLDyKtDVCMB311mOTGg==';lang=en;att=1-ycHI63cHXIvpuNVQFPl14HlqS4C7HiyLnKgrPAFU;auth_token=ba499e9788c9ba4d7bd5a22fd24327f5058da2d4;ct0=b86fb5f0515528aca84644829cdf3b9aa58e505e3000b1755d2f8c2e0453746521219ba508d27f8840470811f8b73485b983a7430df1e572cc35d9a8d0aa068923bc4a992b9509bae1d2668494af3a06;gt=1750018407460897212;_ga=GA1.2.1402762415.1706071873;kdt=oddzwALPLG4FY7nHIjRSrRt5qEXIEbT72YjAPBXg;_gid=GA1.2.678308757.1706071873;twid=u%3D1745514902863929344;guest_id=v1%3A170607187673692322;guest_id_ads=v1%3A170607187673692322;_twitter_sess=BAh7CSIKZmxhc2hJQzonQWN0aW9uQ29udHJvbGxlcjo6Rmxhc2g6OkZsYXNo%250ASGFzaHsABjoKQHVzZWR7ADoPY3JlYXRlZF9hdGwrCDL1zjmNAToMY3NyZl9p%250AZCIlZWI0NDFjNzBkMjgzMWE0ZTFiZDU5MTU1ZTE0ZDA2ZDE6B2lkIiU3Zjdh%250AYTFkYzJiMDQ4YWJlZDhlMzYyMTE5ZGI0YWJlYg%253D%253D--11a182538497f43357f1bdfbbd59fac05bc17db1;guest_id_marketing=v1%3A170607187673692322"},
{"cookes":"personalization_id='v1_dHHFLDyKtDVCMB311mOTGg==';lang=en;att=1-ycHI63cHXIvpuNVQFPl14HlqS4C7HiyLnKgrPAFU;auth_token=ba499e9788c9ba4d7bd5a22fd24327f5058da2d4;ct0=b86fb5f0515528aca84644829cdf3b9aa58e505e3000b1755d2f8c2e0453746521219ba508d27f8840470811f8b73485b983a7430df1e572cc35d9a8d0aa068923bc4a992b9509bae1d2668494af3a06;gt=1750018407460897212;_ga=GA1.2.1402762415.1706071873;kdt=oddzwALPLG4FY7nHIjRSrRt5qEXIEbT72YjAPBXg;_gid=GA1.2.678308757.1706071873;twid=u%3D1745514902863929344;guest_id=v1%3A170607187673692322;guest_id_ads=v1%3A170607187673692322;_twitter_sess=BAh7CSIKZmxhc2hJQzonQWN0aW9uQ29udHJvbGxlcjo6Rmxhc2g6OkZsYXNo%250ASGFzaHsABjoKQHVzZWR7ADoPY3JlYXRlZF9hdGwrCDL1zjmNAToMY3NyZl9p%250AZCIlZWI0NDFjNzBkMjgzMWE0ZTFiZDU5MTU1ZTE0ZDA2ZDE6B2lkIiU3Zjdh%250AYTFkYzJiMDQ4YWJlZDhlMzYyMTE5ZGI0YWJlYg%253D%253D--11a182538497f43357f1bdfbbd59fac05bc17db1;guest_id_marketing=v1%3A170607187673692322"},
{"cookes":"personalization_id='v1_dHHFLDyKtDVCMB311mOTGg==';lang=en;att=1-ycHI63cHXIvpuNVQFPl14HlqS4C7HiyLnKgrPAFU;auth_token=ba499e9788c9ba4d7bd5a22fd24327f5058da2d4;ct0=b86fb5f0515528aca84644829cdf3b9aa58e505e3000b1755d2f8c2e0453746521219ba508d27f8840470811f8b73485b983a7430df1e572cc35d9a8d0aa068923bc4a992b9509bae1d2668494af3a06;gt=1750018407460897212;_ga=GA1.2.1402762415.1706071873;kdt=oddzwALPLG4FY7nHIjRSrRt5qEXIEbT72YjAPBXg;_gid=GA1.2.678308757.1706071873;twid=u%3D1745514902863929344;guest_id=v1%3A170607187673692322;guest_id_ads=v1%3A170607187673692322;_twitter_sess=BAh7CSIKZmxhc2hJQzonQWN0aW9uQ29udHJvbGxlcjo6Rmxhc2g6OkZsYXNo%250ASGFzaHsABjoKQHVzZWR7ADoPY3JlYXRlZF9hdGwrCDL1zjmNAToMY3NyZl9p%250AZCIlZWI0NDFjNzBkMjgzMWE0ZTFiZDU5MTU1ZTE0ZDA2ZDE6B2lkIiU3Zjdh%250AYTFkYzJiMDQ4YWJlZDhlMzYyMTE5ZGI0YWJlYg%253D%253D--11a182538497f43357f1bdfbbd59fac05bc17db1;guest_id_marketing=v1%3A170607187673692322"},
{"cookes":"personalization_id='v1_dHHFLDyKtDVCMB311mOTGg==';lang=en;att=1-ycHI63cHXIvpuNVQFPl14HlqS4C7HiyLnKgrPAFU;auth_token=ba499e9788c9ba4d7bd5a22fd24327f5058da2d4;ct0=b86fb5f0515528aca84644829cdf3b9aa58e505e3000b1755d2f8c2e0453746521219ba508d27f8840470811f8b73485b983a7430df1e572cc35d9a8d0aa068923bc4a992b9509bae1d2668494af3a06;gt=1750018407460897212;_ga=GA1.2.1402762415.1706071873;kdt=oddzwALPLG4FY7nHIjRSrRt5qEXIEbT72YjAPBXg;_gid=GA1.2.678308757.1706071873;twid=u%3D1745514902863929344;guest_id=v1%3A170607187673692322;guest_id_ads=v1%3A170607187673692322;_twitter_sess=BAh7CSIKZmxhc2hJQzonQWN0aW9uQ29udHJvbGxlcjo6Rmxhc2g6OkZsYXNo%250ASGFzaHsABjoKQHVzZWR7ADoPY3JlYXRlZF9hdGwrCDL1zjmNAToMY3NyZl9p%250AZCIlZWI0NDFjNzBkMjgzMWE0ZTFiZDU5MTU1ZTE0ZDA2ZDE6B2lkIiU3Zjdh%250AYTFkYzJiMDQ4YWJlZDhlMzYyMTE5ZGI0YWJlYg%253D%253D--11a182538497f43357f1bdfbbd59fac05bc17db1;guest_id_marketing=v1%3A170607187673692322"}
]


    def get_profile_uid(self,cookies,user_name,headers):
            try:
                params = {
                'variables': '{"screen_name":"%s"}'%(user_name),
                }
                response = requests.get(
                    'https://twitter.com/i/api/graphql/_pnlqeTOtnpbIL9o-fS_pg/ProfileSpotlightsQuery',
                    params=params,cookies=cookies,headers=headers)
                data=(response.json())
                rest_id = data['data']['user_result_by_screen_name']['result']['rest_id']
                return rest_id
            except : return "invaid"

    def felteringx(self,post_url,reaction_numbr,connnt_num,chaption,viwes,reaction_limite,viwes_limite,comment_limite,date_post):
        try:
            if int(reaction_numbr)>=int(reaction_limite) and int(connnt_num) >= int(comment_limite) and int(viwes) >= int(viwes_limite):
                self.data_profile.append({"post_url" : post_url,
            "date_of_post": date_post,
            "tweet": chaption,
            "likes":reaction_numbr,
            "comments": connnt_num,
            "views":viwes})
        except:pass

    def scretpt(self,loads_data,reaction_limite,viwes_limite,comment_limite):
        r"""
        This function parsing All data from the Responce or Inputed Text
        """
        try:
            entry_id = loads_data["data"]["user"]["result"]["timeline_v2"]["timeline"]["instructions"][1]["entries"]
            for data in entry_id:
                try:
                    date_post=data["content"]["itemContent"]["tweet_results"]["result"]["legacy"]["created_at"]
                    connnt_num=data["content"]["itemContent"]["tweet_results"]["result"]["legacy"]["reply_count"]
                    chaption=data["content"]["itemContent"]["tweet_results"]["result"]["legacy"]["full_text"]
                    reaction_numbr=data["content"]["itemContent"]["tweet_results"]["result"]["legacy"]["favorite_count"]
                    viwes=data["content"]["itemContent"]["tweet_results"]["result"]["views"]["count"]
                    post_url=data["content"]["itemContent"]["tweet_results"]["result"]["legacy"]["entities"]["media"][0]["expanded_url"]
                    if int(reaction_numbr)>=int(reaction_limite) and int(connnt_num) >= int(comment_limite) and int(viwes) >= int(viwes_limite):
                        self.data_profile.append({"post_url" : post_url,
            "date_of_post": date_post,
            "tweet": chaption,
            "likes":reaction_numbr,
            "comments": connnt_num,
            "views":viwes})
                    #felteringx(post_url,reaction_numbr,connnt_num,chaption,viwes,reaction_limite,viwes_limite,comment_limite,date_post.replace('+0000',''))
                    #felteringx(post_url,reaction_numbr,connnt_num,chaption,viwes,reaction_limite,viwes_limite,comment_limite,date_post)
                except:pass
                #data_profile.append([post_url,reaction_numbr,connnt_num,chaption,viwes])
        except Exception as e:print("Ecxeption:",e);pass

    def loping(self,rest_id,user_name,tweet_text,cookies,reaction_limite,viwes_limite,comment_limite,nb_tweets,headers):
        # global messag,lop_time
        self.lop_time+=1
        self.scretpt(tweet_text.json(),reaction_limite,viwes_limite,comment_limite)
        r"""
        this a lop for send request gto get more data or Scrolling
        """
        try:
            cursor=re.findall('"value":"(.*?)","cursorType',str(tweet_text.text))[1]
            params = {
                'variables': '{"userId":"%s","count":100,"cursor":"%s","includePromotedContent":true,"withQuickPromoteEligibilityTweetFields":true,"withVoice":true,"withV2Timeline":true}'%(rest_id,cursor),
                'features': '{"responsive_web_graphql_exclude_directive_enabled":true,"verified_phone_label_enabled":false,"creator_subscriptions_tweet_preview_api_enabled":true,"responsive_web_graphql_timeline_navigation_enabled":true,"responsive_web_graphql_skip_user_profile_image_extensions_enabled":false,"c9s_tweet_anatomy_moderator_badge_enabled":true,"tweetypie_unmention_optimization_enabled":true,"responsive_web_edit_tweet_api_enabled":true,"graphql_is_translatable_rweb_tweet_is_translatable_enabled":true,"view_counts_everywhere_api_enabled":true,"longform_notetweets_consumption_enabled":true,"responsive_web_twitter_article_tweet_consumption_enabled":false,"tweet_awards_web_tipping_enabled":false,"freedom_of_speech_not_reach_fetch_enabled":true,"standardized_nudges_misinfo":true,"tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled":true,"rweb_video_timestamps_enabled":true,"longform_notetweets_rich_text_read_enabled":true,"longform_notetweets_inline_media_enabled":true,"responsive_web_media_download_video_enabled":false,"responsive_web_enhance_cards_enabled":false}',
            }
            response = requests.get(
                'https://twitter.com/i/api/graphql/NBWKw7od2So5qClZpLyQ0w/UserTweets',
                params=params,cookies=cookies,headers=headers,allow_redirects=False)
            s=len(self.data_profile)
            if response.status_code ==200:
                if self.lop_time<self.loping_limite:
                    if s > int(nb_tweets):
                        messag = "Done"
                        return messag
                    else:
                        self.loping(rest_id,user_name,response,cookies,reaction_limite,viwes_limite,comment_limite,nb_tweets,headers)
                else:
                    messag = "Done"
                    return messag
            if response.status_code >=400:
                self.het_coookes(user_name,cookies,reaction_limite,viwes_limite,comment_limite,nb_tweets)
        except Exception as messag: self.het_coookes(user_name,cookies,reaction_limite,viwes_limite,comment_limite,nb_tweets)

    def screpeing_profile_post(self,user_name,cookies,reaction_limite,viwes_limite,comment_limite,nb_tweets):  #seach fast page and get data
        try:
            headers = {'authority': 'twitter.com',
            'accept': '*/*','accept-language': 'en-US,en;q=0.9,id;q=0.8,bn;q=0.7','authorization': 'Bearer AAAAAAAAAAAAAAAAAAAAANRILgAAAAAAnNwIzUejRCOuH5E6I8xnZz4puTs%3D1Zv7ttfk8LF81IUq16cHjhLTvJu4FA33AGWWjCpTnA',
            'content-type': 'application/json','referer': 'https://twitter.com/Haqiqatjou','sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120", "Google Chrome";v="120"',
            'sec-ch-ua-mobile': '?0','sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'empty','sec-fetch-mode': 'cors','sec-fetch-site': 'same-origin',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',#W_ueragnt(),
            'x-client-transaction-id': 'BVz3kb2LqtGYEhSPp3wEynvqiYCGRff9SjF37JH8htWXjiV5EGmxJM1qfuQKTa5UksI2VwTpdzt8BMp7gReDTRzgyOj4BA',
            'x-client-uuid': 'd145651c-dfcd-4e30-a8fd-abd1e72f3f86',
            'x-twitter-active-user': 'yes','x-twitter-auth-type': 'OAuth2Session','x-twitter-client-language': 'en',
            'x-csrf-token':cookies['ct0']}
            self.data_profile.clear()
            rest_id=self.get_profile_uid(cookies,user_name,headers)
            if "invaid" in rest_id:
                self.het_coookes(user_name,cookies,reaction_limite,viwes_limite,comment_limite,nb_tweets)
            else:
                params = {
                'variables': '{"userId":"%s","count":20,"includePromotedContent":true,"withQuickPromoteEligibilityTweetFields":true,"withVoice":true,"withV2Timeline":true}'%(rest_id),
                'features': '{"responsive_web_graphql_exclude_directive_enabled":true,"verified_phone_label_enabled":false,"creator_subscriptions_tweet_preview_api_enabled":true,"responsive_web_graphql_timeline_navigation_enabled":true,"responsive_web_graphql_skip_user_profile_image_extensions_enabled":false,"c9s_tweet_anatomy_moderator_badge_enabled":true,"tweetypie_unmention_optimization_enabled":true,"responsive_web_edit_tweet_api_enabled":true,"graphql_is_translatable_rweb_tweet_is_translatable_enabled":true,"view_counts_everywhere_api_enabled":true,"longform_notetweets_consumption_enabled":true,"responsive_web_twitter_article_tweet_consumption_enabled":false,"tweet_awards_web_tipping_enabled":false,"freedom_of_speech_not_reach_fetch_enabled":true,"standardized_nudges_misinfo":true,"tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled":true,"rweb_video_timestamps_enabled":true,"longform_notetweets_rich_text_read_enabled":true,"longform_notetweets_inline_media_enabled":true,"responsive_web_media_download_video_enabled":false,"responsive_web_enhance_cards_enabled":false}',}
                tweet_text = requests.get('https://twitter.com/i/api/graphql/NBWKw7od2So5qClZpLyQ0w/UserTweets',params=params,cookies=cookies,headers=headers)
                if tweet_text.status_code==200:
                    thread1 = threading.Thread(target=self.loping, args=(rest_id,user_name,tweet_text,cookies,reaction_limite,viwes_limite,comment_limite,nb_tweets,headers))
                    thread1.start()
                    thread1.join()
                elif tweet_text.status_code>=400:
                    self.screpeing_profile_post(user_name,cookies,reaction_limite,viwes_limite,comment_limite,nb_tweets)
                if "Done" in messag:
                    return self.data_profile
                else:
                    return  "Something Is Wrong Or Invaid Cookes"
        except Exception as e: return e

    def het_coookes(self,user_name,cookies,reaction_limite,viwes_limite,comment_limite,nb_tweets):
        r"""
        If gets any error Change a new cookes and send all data as new on searching function
        """
        formatted_cookies = ";".join([f"{cookie['name']}={cookie['value']}" for cookie in cookies])
        data_list = self.cookies_file
        cookes = [entry['cookes'] for entry in data_list]
        cookes.remove(formatted_cookies)
        cooki=random.choice(cookes)
        parsed_cookies = parse_qs(cooki.replace(' ',''), separator=';')
        cookiesx= {key: value[0] for key, value in parsed_cookies.items()}
        self.screpeing_profile_post(user_name,cookiesx,reaction_limite,viwes_limite,comment_limite,nb_tweets)

    def felteringx(self,post_url,reaction_numbr,connnt_num,chaption,viwes,reaction_limite,viwes_limite,comment_limite,date_post):
        r"""
        from the getting data use a logic(>=) create a list of json
        """
        try:
            #print(post_url
            if int(reaction_numbr)>=int(reaction_limite) and int(connnt_num) >= int(comment_limite) and int(viwes) >= int(viwes_limite):
                self.search_data.append({"post_url" : post_url,
            "date_of_post": date_post,
            "tweet": chaption,
            "likes":reaction_numbr,
            "comments": connnt_num,
            "views":viwes})
        except:pass

    def parsing(self,loads_data,reaction_limite,viwes_limite,comment_limite):
        r"""
        This function parsing All data from the Responce or Inputed Text
        """
        try:
            entry_id = loads_data["data"]["search_by_raw_query"]["search_timeline"]["timeline"]["instructions"][0]["entries"]
            for data in entry_id:
                try:
                    date_post=data["content"]["itemContent"]["tweet_results"]["result"]["legacy"]["created_at"]
                    connnt_num=data["content"]["itemContent"]["tweet_results"]["result"]["legacy"]["reply_count"]
                    chaption=data["content"]["itemContent"]["tweet_results"]["result"]["legacy"]["full_text"]
                    reaction_numbr=data["content"]["itemContent"]["tweet_results"]["result"]["legacy"]["favorite_count"]
                    viwes=data["content"]["itemContent"]["tweet_results"]["result"]["views"]["count"]
                    post_url=data["content"]["itemContent"]["tweet_results"]["result"]["legacy"]["entities"]["media"][0]["expanded_url"]
                    self.felteringx(post_url,reaction_numbr,connnt_num,chaption,viwes,reaction_limite,viwes_limite,comment_limite,date_post)
                except Exception as e :
                    # print(data)
                    # # input()
                    # with open('parsing.json',"w",encoding="utf-8") as file:
                    #     json_data = json.dump(data ,file ,ensure_ascii=False, indent=4)
                    #     file.close()
                    print("Parsing Exceptio",e)
                    # input()
        except:pass

    def loping_serch(self,tweet_text,cookies,reaction_limite,viwes_limite,comment_limite,nb_tweets,chatagory,headers):
        self.parsing(tweet_text.json(),reaction_limite,viwes_limite,comment_limite)
        global messag,lop_time
        self.lop_time+=1
        """
        this a lop for send request gto get more data or Scrolling
        """
        try:
            cursor=re.findall('"TimelineTimelineCursor","value":"(.*?)","cursorType',str(tweet_text.text))[1]
            # print(cursor)
            params = {
            'variables': '{"rawQuery":"%s","count":50,"cursor":"%s","querySource":"recent_search_click","product":"Top"}'%(chatagory,cursor),
            'features': '{"responsive_web_graphql_exclude_directive_enabled":true,"verified_phone_label_enabled":false,"creator_subscriptions_tweet_preview_api_enabled":true,"responsive_web_graphql_timeline_navigation_enabled":true,"responsive_web_graphql_skip_user_profile_image_extensions_enabled":false,"c9s_tweet_anatomy_moderator_badge_enabled":true,"tweetypie_unmention_optimization_enabled":true,"responsive_web_edit_tweet_api_enabled":true,"graphql_is_translatable_rweb_tweet_is_translatable_enabled":true,"view_counts_everywhere_api_enabled":true,"longform_notetweets_consumption_enabled":true,"responsive_web_twitter_article_tweet_consumption_enabled":false,"tweet_awards_web_tipping_enabled":false,"freedom_of_speech_not_reach_fetch_enabled":true,"standardized_nudges_misinfo":true,"tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled":true,"rweb_video_timestamps_enabled":true,"longform_notetweets_rich_text_read_enabled":true,"longform_notetweets_inline_media_enabled":true,"responsive_web_media_download_video_enabled":false,"responsive_web_enhance_cards_enabled":false}',
            }
            response = requests.get('https://twitter.com/i/api/graphql/PaIcTAgMdfWySgs3aVU5TA/SearchTimeline', params=params,cookies=cookies,headers=headers,)
            if response.status_code ==200:
                s=len(self.search_data)
                if self.lop_time<self.loping_limite:
                    if s >= int(nb_tweets):
                        messag = "Done"
                        return messag
                    else:
                        self.loping_serch(response,cookies,reaction_limite,viwes_limite,comment_limite,nb_tweets,chatagory,headers)
                else:messag = "Done"
            if response.status_code >=400:
                self.het_coookes_search(chatagory,reaction_limite,viwes_limite,comment_limite,nb_tweets)
        except Exception as e:
            self.het_coookes_search(chatagory,reaction_limite,viwes_limite,comment_limite,nb_tweets)
            return e

    def het_coookes_search(self,chatagory,reaction_limite,viwes_limite,comment_limite,nb_tweets,cookes_od):
        r"""
        If gets any error Change a new cookes and send all data as new on searching function
        """
        formatted_cookies = ";".join([f"{cookie['name']}={cookie['value']}" for cookie in cookes_od])
        data_list = self.cookies_file
        cookes = [entry['cookes'] for entry in data_list]
        cookes.remove(formatted_cookies)
        cooki=random.choice(cookes)
        parsed_cookies = parse_qs(cooki.replace(' ',''), separator=';')
        cookiesx= {key: value[0] for key, value in parsed_cookies.items()}
        self.search_Top(cookiesx,chatagory,reaction_limite,viwes_limite,comment_limite,nb_tweets)

    def search_Top(self,cookies,chatagory,reaction_limite,viwes_limite,comment_limite,nb_tweets):
        self.search_data.clear()
        headers = {'authority': 'twitter.com',
        'accept': '*/*','accept-language': 'en-US,en;q=0.9,id;q=0.8,bn;q=0.7','authorization': 'Bearer AAAAAAAAAAAAAAAAAAAAANRILgAAAAAAnNwIzUejRCOuH5E6I8xnZz4puTs%3D1Zv7ttfk8LF81IUq16cHjhLTvJu4FA33AGWWjCpTnA',
        'content-type': 'application/json','referer': 'https://twitter.com/Haqiqatjou','sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120", "Google Chrome";v="120"',
        'sec-ch-ua-mobile': '?0','sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty','sec-fetch-mode': 'cors','sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',#W_ueragnt(),
        'x-client-transaction-id': 'BVz3kb2LqtGYEhSPp3wEynvqiYCGRff9SjF37JH8htWXjiV5EGmxJM1qfuQKTa5UksI2VwTpdzt8BMp7gReDTRzgyOj4BA',
        'x-client-uuid': 'd145651c-dfcd-4e30-a8fd-abd1e72f3f86',
        'x-twitter-active-user': 'yes','x-twitter-auth-type': 'OAuth2Session','x-twitter-client-language': 'en',
        'x-csrf-token':cookies['ct0'] ,
                }
        params = {
        'variables': '{"rawQuery":"%s","count":200,"querySource":"recent_search_click","product":"Top"}'%(chatagory),
        'features': '{"responsive_web_graphql_exclude_directive_enabled":true,"verified_phone_label_enabled":false,"creator_subscriptions_tweet_preview_api_enabled":true,"responsive_web_graphql_timeline_navigation_enabled":true,"responsive_web_graphql_skip_user_profile_image_extensions_enabled":false,"c9s_tweet_anatomy_moderator_badge_enabled":true,"tweetypie_unmention_optimization_enabled":true,"responsive_web_edit_tweet_api_enabled":true,"graphql_is_translatable_rweb_tweet_is_translatable_enabled":true,"view_counts_everywhere_api_enabled":true,"longform_notetweets_consumption_enabled":true,"responsive_web_twitter_article_tweet_consumption_enabled":false,"tweet_awards_web_tipping_enabled":false,"freedom_of_speech_not_reach_fetch_enabled":true,"standardized_nudges_misinfo":true,"tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled":true,"rweb_video_timestamps_enabled":true,"longform_notetweets_rich_text_read_enabled":true,"longform_notetweets_inline_media_enabled":true,"responsive_web_media_download_video_enabled":false,"responsive_web_enhance_cards_enabled":false}',
        }
        response = requests.get('https://twitter.com/i/api/graphql/HgiQ8U_E6g-HE_I6Pp_2UA/SearchTimeline',
            params=params,cookies=cookies,headers=headers,)
        if response.status_code ==200:
            self.loping_serch(response,cookies,reaction_limite,viwes_limite,comment_limite,nb_tweets,chatagory,headers)
        if response.status_code >=400:
            self.search_Top(cookies,chatagory,reaction_limite,viwes_limite,comment_limite,nb_tweets)
        if "Done" in messag:
            return self.search_data
        else:
            return "Something Is Wrong Or Invaid Cookes"


    #xx=search_Top(cookies,keywords,reaction_limite,viwes_limite,comment_limite,nb_tweets)
    # chatagory='global warming'               # keyword name wich are scraping
    # nb_tweets=15                     # the number of data you want
    # reaction_limite=0
    # viwes_limite=0
    # comment_limite=0
    # keywords=["IOCL","Electrosteel Castings", "ITC", "COAL India", "MRF"]
    # type_search='topics'


    # def cookes(self,x):
    # global cookies
    data_list = cookies_file
    cookes = [entry['cookes'] for entry in data_list]
    cooki=random.choice(cookes)
    parsed_cookies = parse_qs(cooki.replace(' ',''), separator=';')
    cookies= {key: value[0] for key, value in parsed_cookies.items()}

    # @cookes
    def c(self):
        pass

    def main(self,type_search, keywords, reaction_limite,viwes_limite,comment_limite,nb_tweets):
        # print("hiiii")
        # print(keywords)
        tweets = []
        for keyword in keywords:
            # try:
                # print(type_search)
                if 'profile' in str(type_search).lower():
                    try:
                        sleep(0.2)
                        global lop_time
                        self.lop_time=0
                        tweet=self.screpeing_profile_post(keyword,self.cookies,reaction_limite,viwes_limite,comment_limite,nb_tweets)
                        #print(tweet)
                        new_data = [{
                            "type": "username",
                            "keyword": keyword,
                            "tweets": []
                        }]
                        new_data[0]["tweets"].extend(tweet)
                        tweets.extend(new_data)
                    except:pass
                        #return data_profile
                else:
                    try:
                        # print("hi")
                        tweet=self.search_Top(self.cookies,keyword,reaction_limite,viwes_limite,comment_limite,nb_tweets)
                        new_data = [{
                            "type": "topic",
                            "keyword": keyword,
                            "tweets": []
                        }]
                        new_data[0]["tweets"].extend(tweet)
                        tweets.extend(new_data)
                    except Exception as e :
                        print(e)
                #tweets += [tweet]
            # except Exception as e :print(e)
        return tweets

    # new_data=main(type_search, keywords, reaction_limite,viwes_limite,comment_limite,nb_tweets)

