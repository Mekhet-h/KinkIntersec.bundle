# Kink.com
import re 
import urllib2

# URLS
EXC_BASEURL = 'http://www.kinkondemand.com/'
EXC_SEARCH_MOVIES = EXC_BASEURL + '/kod/search.jsp?search=%s'
EXC_MOVIE_INFO = EXC_BASEURL + 'kod/shoot/%s'

def Start():
  HTTP.CacheTime = CACHE_1DAY
  HTTP.Headers['User-Agent'] = 'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.2; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0)'

def file_exists(url):
  request = urllib2.Request(url)
  request.get_method = lambda : 'HEAD'
  try:
    response = urllib2.urlopen(request)
    return True
  except:
    return False

class KinkIntersec(Agent.Movies):
  name = 'KinkIntersec'
  languages = [Locale.Language.English]
  accepts_from = ['com.plexapp.agents.localmedia']
  primary_provider = True

  def search(self, results, media, lang, manual):

    title = media.name
    title = title.lower()
    #if media.primary_metadata is not None:
    #  title = media.primary_metadata.title

    # File Format: XX_1111-%%%%%%%%
    # e.g EB_7572-Isis Felony will extract "EB" "7572"
    #episodeMatch = re.match('([a-zA-Z]{1,})_(\d{1,})-(.{1,})',title)

    # if file starts with episode id, just go directly to that episode
    #if episodeMatch is not None:
    #  studioID = episodeMatch.group(1)
    #  if studioID is "HA" or studioID is "IR" or studioID is "IS" or studioID is "RB" or studioID is "SB" or studioID is "TG":
    #    year = episodeMatch.group(2)
    #    episodeId = episodeMatch.group(3)
    #  else:
    #    year = "0"
    #    episodeId = episodeMatch.group(2)
      
    #  Log.Debug("Studio: " + studioID + " Episode: " + episodeId + " Year: " + year)
    results.Append(MetadataSearchResult(id = title, name = title, score = 90, lang = lang))

    results.Sort('score', descending=True)

  def update(self, metadata, media, lang, force):
    splitID = metadata.id.split('_')
    
    if len(splitID[0]) > 3 :
      splitID = metadata.id.split(' ')
      
    #Log.Debug(splitID[3][2:])
    #for string in splitID:
    #  Log.Debug(string)
    
    if splitID[0] == 'sb' or splitID[0] == 'ir' or splitID[0] == 'rb' or splitID[0] == 'ha' or splitID[0] == 'tg':
      series = ""
      if splitID[0] == 'sb':
        url = "http://www.sexuallybroken.com/sexual/bondage/trailer.php?y=" + splitID[1] + "&p=" + splitID[2] + "_" + splitID[3]
        thumbpUrl2 = "http://promo.sexuallybroken.com/images/" + splitID[1] + "/" + splitID[2] + "_" + splitID[3] + "/01.jpg"
        thumbpUrl4 = "http://promo.sexuallybroken.com/images/" + splitID[1] + "/" + splitID[2] + "_" + splitID[3] + "/trailer_noplay.jpg"
        thumbpUrl1 = "http://promo.sexuallybroken.com/images/" + splitID[1] + "/" + splitID[2] + "_" + splitID[3] + "/poster.jpg"
        thumbpUrl3 = "http://promo.sexuallybroken.com/images/" + splitID[1] + "/" + splitID[2] + "_" + splitID[3] + "/" + splitID[3][2:] + "_01.jpg"
        series = "SexuallyBroken.com"
      elif splitID[0] == 'ir':
        if len(splitID) == 5:
          url = "http://www.infernalrestraints.com/device/bondage/trailer.php?y=" + splitID[1] + "&p=" + splitID[2] + "_" + splitID[3] + "_" + splitID[4]
          thumbpUrl2 = "http://promo.infernalrestraints.com/images/" + splitID[1] + "/" + splitID[2] + "_" + splitID[3] + "_" + splitID[4] + "/01.jpg"
          thumbpUrl4 = "http://promo.infernalrestraints.com/images/" + splitID[1] + "/" + splitID[2] + "_" + splitID[3] + "_" + splitID[4] + "/trailer_noplay.jpg"
          thumbpUrl1 = "http://promo.infernalrestraints.com/images/" + splitID[1] + "/" + splitID[2] + "_" + splitID[3] + "_" + splitID[4] + "/poster.jpg"
          thumbpUrl3 = "http://promo.infernalrestraints.com/images/" + splitID[1] + "/" + splitID[2] + "_" + splitID[3] + "_" + splitID[4] + "/" + splitID[3][2:] + splitID[4] + "_01.jpg"
        else:
          url = "http://www.infernalrestraints.com/device/bondage/trailer.php?y=" + splitID[1] + "&p=" + splitID[2] + "_" + splitID[3]
          thumbpUrl2 = "http://promo.infernalrestraints.com/images/" + splitID[1] + "/" + splitID[2] + "_" + splitID[3] + "/01.jpg"
          thumbpUrl4 = "http://promo.infernalrestraints.com/images/" + splitID[1] + "/" + splitID[2] + "_" + splitID[3] + "/trailer_noplay.jpg"
          thumbpUrl1 = "http://promo.infernalrestraints.com/images/" + splitID[1] + "/" + splitID[2] + "_" + splitID[3] + "/poster.jpg"
          thumbpUrl3 = "http://promo.infernalrestraints.com/images/" + splitID[1] + "/" + splitID[2] + "_" + splitID[3] + "/" + splitID[3][2:] + "_01.jpg"
        series = "InfernalRestraints.com"
      elif splitID[0] == 'rb':
        if len(splitID) == 5:
          url = "http://www.realtimebondage.com/live/bondage/trailer.php?y=" + splitID[1] + "&p=" + splitID[2] + "_" + splitID[3] + "_" + splitID[4]
          thumbpUrl2 = "http://promo.realtimebondage.com/images/" + splitID[1] + "/" + splitID[2] + "_" + splitID[3] + "_" + splitID[4] + "/01.jpg"
          thumbpUrl4 = "http://promo.realtimebondage.com/images/" + splitID[1] + "/" + splitID[2] + "_" + splitID[3] + "_" + splitID[4] + "/trailer_noplay.jpg"
          thumbpUrl1 = "http://promo.realtimebondage.com/images/" + splitID[1] + "/" + splitID[2] + "_" + splitID[3] + "_" + splitID[4] + "/poster.jpg"
          thumbpUrl3 = "http://promo.realtimebondage.com/images/" + splitID[1] + "/" + splitID[2] + "_" + splitID[3] + "_" + splitID[4] + "/" + splitID[3][2:] + splitID[4] + "_01.jpg"
        else:
          url = "http://www.realtimebondage.com/live/bondage/trailer.php?y=" + splitID[1] + "&p=" + splitID[2] + "_" + splitID[3]
          thumbpUrl2 = "http://promo.realtimebondage.com/images/" + splitID[1] + "/" + splitID[2] + "_" + splitID[3] + "/01.jpg"
          thumbpUrl4 = "http://promo.realtimebondage.com/images/" + splitID[1] + "/" + splitID[2] + "_" + splitID[3] + "/trailer_noplay.jpg"
          thumbpUrl1 = "http://promo.realtimebondage.com/images/" + splitID[1] + "/" + splitID[2] + "_" + splitID[3] + "/poster.jpg"
          thumbpUrl3 = "http://promo.realtimebondage.com/images/" + splitID[1] + "/" + splitID[2] + "_" + splitID[3] + "/" + splitID[3][2:] + "_01.jpg"
        series = "RealTimeBondage.com"
      elif splitID[0] == 'ha':
        if len(splitID) == 5:
          url = "http://www.hardtied.com/hogtied/bondage/trailer.php?y=" + splitID[1] + "&p=" + splitID[2] + "_" + splitID[3] + "_" + splitID[4]
          thumbpUrl2 = "http://promo.hardtied.com/images/" + splitID[1] + "/" + splitID[2] + "_" + splitID[3] + "_" + splitID[4] + "/01.jpg"
          thumbpUrl4 = "http://promo.hardtied.com/images/" + splitID[1] + "/" + splitID[2] + "_" + splitID[3] + "_" + splitID[4] + "/trailer_noplay.jpg"
          thumbpUrl1 = "http://promo.hardtied.com/images/" + splitID[1] + "/" + splitID[2] + "_" + splitID[3] + "_" + splitID[4] + "/poster.jpg"
          thumbpUrl3 = "http://promo.hardtied.com/images/" + splitID[1] + "/" + splitID[2] + "_" + splitID[3] + "_" + splitID[4] + "/" + splitID[3][2:] + splitID[4] + "_01.jpg"
        else:
          url = "http://www.hardtied.com/hogtied/bondage/trailer.php?y=" + splitID[1] + "&p=" + splitID[2] + "_" + splitID[3]
          thumbpUrl2 = "http://promo.hardtied.com/images/" + splitID[1] + "/" + splitID[2] + "_" + splitID[3] + "/01.jpg"
          thumbpUrl4 = "http://promo.hardtied.com/images/" + splitID[1] + "/" + splitID[2] + "_" + splitID[3] + "/trailer_noplay.jpg"
          thumbpUrl1 = "http://promo.hardtied.com/images/" + splitID[1] + "/" + splitID[2] + "_" + splitID[3] + "/poster.jpg"
          thumbpUrl3 = "http://promo.hardtied.com/images/" + splitID[1] + "/" + splitID[2] + "_" + splitID[3] + "/" + splitID[3][2:] + "_01.jpg"
        series = "Hardtied.com"
      elif splitID[0] == 'tg':
        if len(splitID) == 5:
          url = "http://www.topgrl.com/female/bondage/trailer.php?y=" + splitID[1] + "&p=" + splitID[2] + "_" + splitID[3] + "_" + splitID[4]
          thumbpUrl2 = "http://promo.topgrl.com/images/" + splitID[1] + "/" + splitID[2] + "_" + splitID[3] + "_" + splitID[4] + "/01.jpg"
          thumbpUrl4 = "http://promo.topgrl.com/images/" + splitID[1] + "/" + splitID[2] + "_" + splitID[3] + "_" + splitID[4] + "/trailer_noplay.jpg"
          thumbpUrl1 = "http://promo.topgrl.com/images/" + splitID[1] + "/" + splitID[2] + "_" + splitID[3] + "_" + splitID[4] + "/poster.jpg"
          thumbpUrl3 = "http://promo.topgrl.com/images/" + splitID[1] + "/" + splitID[2] + "_" + splitID[3] + "_" + splitID[4] + "/" + splitID[3][2:] + splitID[4] + "_01.jpg"
        else:
          url = "http://www.topgrl.com/female/bondage/trailer.php?y=" + splitID[1] + "&p=" + splitID[2] + "_" + splitID[3]
          thumbpUrl2 = "http://promo.topgrl.com/images/" + splitID[1] + "/" + splitID[2] + "_" + splitID[3] + "/01.jpg"
          thumbpUrl4 = "http://promo.topgrl.com/images/" + splitID[1] + "/" + splitID[2] + "_" + splitID[3] + "/trailer_noplay.jpg"
          thumbpUrl1 = "http://promo.topgrl.com/images/" + splitID[1] + "/" + splitID[2] + "_" + splitID[3] + "/poster.jpg"
          thumbpUrl3 = "http://promo.topgrl.com/images/" + splitID[1] + "/" + splitID[2] + "_" + splitID[3] + "/" + splitID[3][2:] + "_01.jpg"
        series = "TopGrl.com"
      metadata.studio = series
      metadata.genres.add(series)
      
      metadata.tagline = series + " – " + splitID[2] + splitID[3][:2]
      
      html = HTML.ElementFromURL(url)
      
      # set movie title to shoot title
      metadata.title = html.xpath('//span[@class="articleTitleText"]/a')[0].text_content()
      
      # set rating to XXX
      metadata.content_rating = 'XXX'
      
      # set movie release date to shoot release date
      try:
        metadata.originally_available_at = Datetime.ParseDate(splitID[3][:2] + "." + splitID[2] + "." + splitID[1]).date()
        metadata.year = metadata.originally_available_at.year
      except: pass
      
      # set poster to the image that intersec choose as preview
      try:
        if file_exists(thumbpUrl1):
          thumbp = HTTP.Request(thumbpUrl1)
          metadata.posters[thumbpUrl1] = Proxy.Media(thumbp)
          #Log.Debug("URL Typ 1 exists!")
        elif file_exists(thumbpUrl4):
          thumbp = HTTP.Request(thumbpUrl4)
          metadata.posters[thumbpUrl4] = Proxy.Media(thumbp)
          #Log.Debug("URL Typ 4 exists!")
        elif file_exists(thumbpUrl2):
          thumbp = HTTP.Request(thumbpUrl2)
          metadata.posters[thumbpUrl2] = Proxy.Media(thumbp)
          #Log.Debug("URL Typ 2 exists!")
        else:
          thumbp = HTTP.Request(thumbpUrl3)
          metadata.posters[thumbpUrl3] = Proxy.Media(thumbp)
          #Log.Debug("URL Typ 3 exists!")
      except: pass
      
      # fill movie art with all images, so they can be used as backdrops
      #try:
      #  imgs = html.xpath('//table[@class="fullViewTable"]//img')
      #  for img in imgs:
      #    thumbUrl = re.sub(r'/h/[0-9]{3,3}/', r'/h/830/', img.get('src'))
      #    thumb = HTTP.Request(thumbUrl)
      #    metadata.art[thumbUrl] = Proxy.Media(thumb)
      #except: pass
      
      # summary
      try:
        metadata.summary = html.xpath('//table[@id="articleText"]//td[@class="articleCopyText"]')[0].text_content()
      except: pass
      
      # starring/director
      try:
        starring = html.xpath('//span[@class="articleTitleText"]')[0].text_content().split('|')
        metadata.roles.clear()
        for i in range(len(starring)-1):
          role = metadata.roles.new() 
          role.actor = starring[i+1].strip(' ')
          Log.Debug(starring[i+1])
      except: pass
    else:
      #for string in splitID:
      #  Log.Debug(string)
      if len(splitID[0]) > 3:
       clipID = splitID[0]
      else:
       clipID = splitID[1]
      html = HTML.ElementFromURL(EXC_MOVIE_INFO % clipID)
      
      seriesLogo = html.xpath('//div[@id="allShootInfo"]//div[@id="justLogo"]//img')
      if len(seriesLogo) > 0:
        series = seriesLogo[0].get('alt')
      else:
        series = html.xpath('//div[@id="allShootInfo"]//div[@id="justLogo"]')[0].text_content().strip('\t\r\n ')
      
      # set movie studio to kink site
      metadata.studio = series
      
      # set movie title to shoot title
      metadata.title = html.xpath('//div[@id="shootHeader"]/h1')[0].text_content() + " (" + clipID + ")"
      
      # set rating to XXX
      metadata.content_rating = 'XXX'
      metadata.genres.add(series)
      
      #set episode ID as tagline for easy visibility
      metadata.tagline = series + " – " + clipID
      
      # set movie release date to shoot release date
      try:
        release_date = html.xpath('//div[@class="titleAndPerformers"]//p')[0].text_content().split('-')[0].strip('\t\r\n')
        metadata.originally_available_at = Datetime.ParseDate(release_date).date()
        metadata.year = metadata.originally_available_at.year
      except: pass
      
      # set poster to the image that kink.com chose as preview
      try:
        thumbselection = html.xpath('//div[@class="titleAndPerformers"]/meta[@itemprop="image"]/@content')[0]
        thumbpUrl = re.sub(r'/h/[0-9]{3,3}/', r'/h/830/', thumbselection)
        thumbp = HTTP.Request(thumbpUrl)
        metadata.posters[thumbpUrl] = Proxy.Media(thumbp)
      except: pass
      
      # fill movie art with all images, so they can be used as backdrops
      try:
        imgs = html.xpath('//table[@class="fullViewTable"]//img')
        for img in imgs:
          thumbUrl = re.sub(r'/h/[0-9]{3,3}/', r'/h/830/', img.get('src'))
          thumb = HTTP.Request(thumbUrl)
          metadata.art[thumbUrl] = Proxy.Media(thumb)
      except: pass
      
      # summary
      try:
        metadata.summary = ""
        summary = html.xpath('//div[@class="shootDescription"]/p[@class="description"]')
        if len(summary) > 0:
          for paragraph in summary:
            metadata.summary = metadata.summary + paragraph.text_content().strip(' \n\r\t').replace('<br>',"\n") + "\n"
          metadata.summary.strip('\n')
      except: pass
      
      # starring/director
      try:
        starring = html.xpath('//div[@class="titleAndPerformers"]//a')
        metadata.directors.clear()
        metadata.roles.clear()
        thedirector = html.xpath('//div[@class="titleAndPerformers"]/meta[@itemprop="director"]/@content')[0]
        metadata.directors.add(thedirector)
        for member in starring:
          role = metadata.roles.new()
          lename = member.text_content().strip(' ')
          role.actor = lename
      except: pass