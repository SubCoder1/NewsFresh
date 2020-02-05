import 'package:flutter/material.dart';
class Upload extends StatefulWidget {
  @override
  _UploadState createState() => _UploadState();
}

class _UploadState extends State<Upload> {
  bool _isFavorited = true;
  int _favoriteCount = 290;

  void _toggleFavorite() {
    setState(() {
      if (_isFavorited) {
        _favoriteCount -= 1;
        _isFavorited = false;
      } else {
        _favoriteCount += 1;
        _isFavorited = true;
      }
    });
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text("Upload news"),
        centerTitle: true,
        backgroundColor: Colors.black54,

        actions: <Widget>[


          IconButton(icon: Icon(Icons.file_upload,textDirection: TextDirection.ltr,), onPressed: null),


        ],

      ),

      body: ListView(
        children: <Widget>[
          Card(shape: RoundedRectangleBorder(
              borderRadius: BorderRadius.circular(16.0)
          ),
            child: ClipRRect(

              child: Image.network("https://www.economist.com/sites/default/files/images/2019/10/articles/main/20191026_ldp502.jpg"),

              borderRadius: BorderRadius.only(

                  topRight: Radius.circular(18.0),

                  topLeft: Radius.circular(18.0),

                  bottomLeft:Radius.circular(18.0),

                  bottomRight: Radius.circular(18.0)

              ),

            ),
          ),
          Padding(padding: EdgeInsets.symmetric(vertical: 8.0,horizontal: 8.0),
            child: Card(
              shape: RoundedRectangleBorder(
                  borderRadius: BorderRadius.circular(16.0)
              ),
              child: Column(
                mainAxisAlignment: MainAxisAlignment.start,
                crossAxisAlignment: CrossAxisAlignment.start,

                children: <Widget>[

                  Text("Anti-CAA stirs in Delhi part of political design: PM Modi".toUpperCase()

                  ),
                  Text(" Prime Minister Narendra Modi in Delhi on Monday slammed the anti-CAA agitators in Shaheen Bagh and other areas saying the protest against the new citizenship law was an experiment and there was a design of politics behind it, which would ruin the national harmony.".toLowerCase(),
                    style: TextStyle(
                        color: Colors.black54
                    ),
                  ),
                  SizedBox(height: 16.0,),
                  Row(
                    children: <Widget>[

                      IconButton(
                        icon: (_isFavorited ? Icon(Icons.favorite) : Icon(
                            Icons.favorite)),
                        color: Color(0xffed1e79),
                        onPressed: _toggleFavorite,
                      ),
                      Text('$_favoriteCount upvote'),
                      IconButton(
                        icon: (_isFavorited ? Icon(Icons.favorite_border) : Icon(
                            Icons.favorite_border)),
                        color: Color(0xffed1e79),
                        onPressed: _toggleFavorite,
                      ),
                      Text('17 downvote   '),
                      Expanded(child: Text("5 Feb,2020")),
                    ],
                  ),
                  Text("~~~ Reputability score: 0.87")
                ],
              ),
            ),
          ),
          Card(shape: RoundedRectangleBorder(
              borderRadius: BorderRadius.circular(16.0)
          ),
            child: ClipRRect(

              child: Image.network("https://www.hindustantimes.com/rf/image_size_960x540/HT/p2/2020/02/02/Pictures/republic-personnel-patrol-celebrations-occasion-chowk-71st_436fcefa-45a2-11ea-bfa0-35d85fc987f6.jpg"),

              borderRadius: BorderRadius.only(

                  topRight: Radius.circular(18.0),

                  topLeft: Radius.circular(18.0),

                  bottomLeft:Radius.circular(18.0),

                  bottomRight: Radius.circular(18.0)

              ),

            ),
          ),
          Padding(padding: EdgeInsets.symmetric(vertical: 8.0,horizontal: 8.0),
            child: Card(
              shape: RoundedRectangleBorder(
                  borderRadius: BorderRadius.circular(16.0)
              ),
              child: Column(
                mainAxisAlignment: MainAxisAlignment.start,
                crossAxisAlignment: CrossAxisAlignment.start,

                children: <Widget>[

                  Text("Kashmir needs a political outreach".toUpperCase()

                  ),
                  Text(" Wednesday marks six months since Parliament effectively nullified Article 370, divided Jammu and Kashmir into two units, and converted both J&K and Ladakh into separate union territories (UTs). This was among the most radical political measures the Bharatiya Janata Party-led government has taken. The government said the move would fully integrate J&K into the Indian Union, and citizens of the region will now enjoy the same rights as citizens elsewhere. The move would also, the government argued, end terrorism.".toLowerCase(),
                    style: TextStyle(
                        color: Colors.black54
                    ),
                  ),
                  SizedBox(height: 16.0,),
                  Row(
                    children: <Widget>[

                      IconButton(
                        icon: (_isFavorited ? Icon(Icons.favorite) : Icon(
                            Icons.favorite)),
                        color: Color(0xffed1e79),
                        onPressed: _toggleFavorite,
                      ),
                      Text('$_favoriteCount 1 upvote'),
                      IconButton(
                        icon: (_isFavorited ? Icon(Icons.favorite_border) : Icon(
                            Icons.favorite_border)),
                        color: Color(0xffed1e79),
                        onPressed: _toggleFavorite,
                      ),
                      Text('8 downvote'),
                      Expanded(child: Text("5 Feb,2020")),
                    ],
                  ),
                  Text("~~~ Reputability score: 0.93")
                ],
              ),
            ),
          ),
          Card(shape: RoundedRectangleBorder(
              borderRadius: BorderRadius.circular(16.0)
          ),
            child: ClipRRect(

              child: Image.network("https://www.aljazeera.com/mritems/imagecache/mbdxxlarge/mritems/Images/2020/2/4/f1e99103152e4b01bee71cb1ba179a37_18.jpg"),

              borderRadius: BorderRadius.only(

                  topRight: Radius.circular(18.0),

                  topLeft: Radius.circular(18.0),

                  bottomLeft:Radius.circular(18.0),

                  bottomRight: Radius.circular(18.0)

              ),

            ),
          ),
          Padding(padding: EdgeInsets.symmetric(vertical: 8.0,horizontal: 8.0),
            child: Card(
              shape: RoundedRectangleBorder(
                  borderRadius: BorderRadius.circular(16.0)
              ),
              child: Column(
                mainAxisAlignment: MainAxisAlignment.start,
                crossAxisAlignment: CrossAxisAlignment.start,

                children: <Widget>[

                  Text("The political cost of the coronavirus outbreak in Hong Kong".toUpperCase()

                  ),
                  Text(" The inadequate actions of the authorities in the face of a major health emergency could cause more social upheaval.".toLowerCase(),
                    style: TextStyle(
                        color: Colors.black54
                    ),
                  ),
                  SizedBox(height: 16.0,),
                  Row(
                    children: <Widget>[

                      IconButton(
                        icon: (_isFavorited ? Icon(Icons.favorite) : Icon(
                            Icons.favorite)),
                        color: Color(0xffed1e79),
                        onPressed: _toggleFavorite,
                      ),
                      Text('$_favoriteCount 2upvote'),
                      IconButton(
                        icon: (_isFavorited ? Icon(Icons.favorite_border) : Icon(
                            Icons.favorite_border)),
                        color: Color(0xffed1e79),
                        onPressed: _toggleFavorite,
                      ),
                      Text('36 downvote   '),
                      Expanded(child: Text("5 Feb,2020")),
                    ],
                  ),
                  Text("~~~ Reputability score: 0.79")
                ],
              ),
            ),
          ),
          Card(shape: RoundedRectangleBorder(
              borderRadius: BorderRadius.circular(16.0)
          ),
            child: ClipRRect(

              child: Image.network("https://akm-img-a-in.tosshub.com/indiatoday/images/story/202002/Modi_1-770x433.jpeg?JixHqZFeK243M7oeG8cB2cPhU0_zivm8"),

              borderRadius: BorderRadius.only(

                  topRight: Radius.circular(18.0),

                  topLeft: Radius.circular(18.0),

                  bottomLeft:Radius.circular(18.0),

                  bottomRight: Radius.circular(18.0)

              ),

            ),
          ),
          Padding(padding: EdgeInsets.symmetric(vertical: 8.0,horizontal: 8.0),
            child: Card(
              shape: RoundedRectangleBorder(
                  borderRadius: BorderRadius.circular(16.0)
              ),
              child: Column(
                mainAxisAlignment: MainAxisAlignment.start,
                crossAxisAlignment: CrossAxisAlignment.start,

                children: <Widget>[

                  Text("Our target is to increase defence exports to Rs 35,000 crore in next 5 years: PM Modi".toUpperCase()

                  ),
                  Text("Prime Minister Narendra Modi on Wednesday said his government's aim is to increase India's defence exports to USD 5 billion in the next five years.".toLowerCase(),
                    style: TextStyle(
                        color: Colors.black54
                    ),
                  ),
                  SizedBox(height: 16.0,),
                  Row(
                    children: <Widget>[

                      IconButton(
                        icon: (_isFavorited ? Icon(Icons.favorite) : Icon(
                            Icons.favorite)),
                        color: Color(0xffed1e79),
                        onPressed: _toggleFavorite,
                      ),
                      Text('$_favoriteCount upvote'),
                      IconButton(
                        icon: (_isFavorited ? Icon(Icons.favorite_border) : Icon(
                            Icons.favorite_border)),
                        color: Color(0xffed1e79),
                        onPressed: _toggleFavorite,
                      ),
                      Text('60 downvote   '),
                      Expanded(child: Text("5 Feb,2020")),
                    ],
                  ),
                  Text("~~~ Reputability score: 0.64")
                ],
              ),
            ),
          ),
          Card(shape: RoundedRectangleBorder(
              borderRadius: BorderRadius.circular(16.0)
          ),
            child: ClipRRect(

              child: Image.network("https://akm-img-a-in.tosshub.com/indiatoday/images/story/202002/PTI1-770x433.jpeg?EV72AHa90GgqTL6KAk8d18HDN9rtmtBU"),

              borderRadius: BorderRadius.only(

                  topRight: Radius.circular(18.0),

                  topLeft: Radius.circular(18.0),

                  bottomLeft:Radius.circular(18.0),

                  bottomRight: Radius.circular(18.0)

              ),

            ),
          ),
          Padding(padding: EdgeInsets.symmetric(vertical: 8.0,horizontal: 8.0),
            child: Card(
              shape: RoundedRectangleBorder(
                  borderRadius: BorderRadius.circular(16.0)
              ),
              child: Column(
                mainAxisAlignment: MainAxisAlignment.start,
                crossAxisAlignment: CrossAxisAlignment.start,

                children: <Widget>[

                  Text("Delhi elections: NRIs fly in to campaign for AAP in capital".toUpperCase()

                  ),
                  Text("Not just the locals but a large number of NRIs too are campaigning for the Aam Aadmi Party in Delhi believing that party chief Arvind Kejriwal will bring in a change in the city. Hundreds of NRIs have flown into the city and are working on the ground as the national capital gears up for the Assembly polls on February 8.".toLowerCase(),
                    style: TextStyle(
                        color: Colors.black54
                    ),
                  ),
                  SizedBox(height: 16.0,),
                  Row(
                    children: <Widget>[

                      IconButton(
                        icon: (_isFavorited ? Icon(Icons.favorite) : Icon(
                            Icons.favorite)),
                        color: Color(0xffed1e79),
                        onPressed: _toggleFavorite,
                      ),
                      Text('$_favoriteCount 3 upvote'),
                      IconButton(
                        icon: (_isFavorited ? Icon(Icons.favorite_border) : Icon(
                            Icons.favorite_border)),
                        color: Color(0xffed1e79),
                        onPressed: _toggleFavorite,
                      ),
                      Text('160 downvote'),
                      Expanded(child: Text("5 Feb,2020")),
                    ],
                  ),
                  Text("~~~ Reputability score: 0.57")
                ],
              ),
            ),
          ),
          Card(shape: RoundedRectangleBorder(
              borderRadius: BorderRadius.circular(16.0)
          ),
            child: ClipRRect(

              child: Image.network("https://www.indiatoday.in/lifestyle/fashion/story/sara-ali-khan-in-off-shoulder-crop-top-and-pants-brings-the-70s-back-for-new-shoot-all-pics-1643538-2020-02-05?utm_source=recengine&utm_medium=web&referral=yes&utm_content=footerstrip-2"),

              borderRadius: BorderRadius.only(

                  topRight: Radius.circular(18.0),

                  topLeft: Radius.circular(18.0),

                  bottomLeft:Radius.circular(18.0),

                  bottomRight: Radius.circular(18.0)

              ),

            ),
          ),
          Padding(padding: EdgeInsets.symmetric(vertical: 8.0,horizontal: 8.0),
            child: Card(
              shape: RoundedRectangleBorder(
                  borderRadius: BorderRadius.circular(16.0)
              ),
              child: Column(
                mainAxisAlignment: MainAxisAlignment.start,
                crossAxisAlignment: CrossAxisAlignment.start,

                children: <Widget>[

                  Text("No family member has anything to do with AAP: Shaheen Bagh shooter Kapil Gujar's father".toUpperCase()

                  ),
                  Text("After the Delhi Police recovered photos of Shaheen Bagh shooter Kapil Gujjar with several senior leaders of the AAP from his mobile phone, his father Gaje Singh said that no member of his family is associated with AAP and that he himself was a member of the BSP till 2012".toLowerCase(),
                    style: TextStyle(
                        color: Colors.black54
                    ),
                  ),
                  SizedBox(height: 16.0,),
                  Row(
                    children: <Widget>[

                      IconButton(
                        icon: (_isFavorited ? Icon(Icons.favorite) : Icon(
                            Icons.favorite)),
                        color: Color(0xffed1e79),
                        onPressed: _toggleFavorite,
                      ),
                      Text('$_favoriteCount upvote'),
                      IconButton(
                        icon: (_isFavorited ? Icon(Icons.favorite_border) : Icon(
                            Icons.favorite_border)),
                        color: Color(0xffed1e79),
                        onPressed: _toggleFavorite,
                      ),
                      Text('17 downvote   '),
                      Expanded(child: Text("5 Feb,2020")),
                    ],
                  ),
                  Text("~~~ Reputability score: 0.87")
                ],
              ),
            ),
          ),
          Card(shape: RoundedRectangleBorder(
              borderRadius: BorderRadius.circular(16.0)
          ),
            child: ClipRRect(

              child: Image.network("https://akm-img-a-in.tosshub.com/indiatoday/images/story/202002/Geforce_now-770x433.jpeg?Yc9UsEG7l5dJQrAchUf7d8UjoxYcFPB4"),

              borderRadius: BorderRadius.only(

                  topRight: Radius.circular(18.0),

                  topLeft: Radius.circular(18.0),

                  bottomLeft:Radius.circular(18.0),

                  bottomRight: Radius.circular(18.0)

              ),

            ),
          ),
          Padding(padding: EdgeInsets.symmetric(vertical: 8.0,horizontal: 8.0),
            child: Card(
              shape: RoundedRectangleBorder(
                  borderRadius: BorderRadius.circular(16.0)
              ),
              child: Column(
                mainAxisAlignment: MainAxisAlignment.start,
                crossAxisAlignment: CrossAxisAlignment.start,

                children: <Widget>[

                  Text("Nvidia’s game streaming service, GeForce Now out of beta, to rival Google Stadia".toUpperCase()

                  ),
                  Text("The Nvidia game streaming platform uses its GeForce graphics cards to power gaming on personal computers, android phones and Shield TVs.".toLowerCase(),
                    style: TextStyle(
                        color: Colors.black54
                    ),
                  ),
                  SizedBox(height: 16.0,),
                  Row(
                    children: <Widget>[

                      IconButton(
                        icon: (_isFavorited ? Icon(Icons.favorite) : Icon(
                            Icons.favorite)),
                        color: Color(0xffed1e79),
                        onPressed: _toggleFavorite,
                      ),
                      Text('$_favoriteCount upvote'),
                      IconButton(
                        icon: (_isFavorited ? Icon(Icons.favorite_border) : Icon(
                            Icons.favorite_border)),
                        color: Color(0xffed1e79),
                        onPressed: _toggleFavorite,
                      ),
                      Text('17 downvote   '),
                      Expanded(child: Text("5 Feb,2020")),
                    ],
                  ),
                  Text("~~~ Reputability score: 0.87")
                ],
              ),
            ),
          ),
          Card(shape: RoundedRectangleBorder(
              borderRadius: BorderRadius.circular(16.0)
          ),
            child: ClipRRect(

              child: Image.network("https://akm-img-a-in.tosshub.com/indiatoday/images/story/202002/alexa-770x433.jpeg?AS7PHtuU3lA04j9w_qCGN1ig1Mca0y.E"),

              borderRadius: BorderRadius.only(

                  topRight: Radius.circular(18.0),

                  topLeft: Radius.circular(18.0),

                  bottomLeft:Radius.circular(18.0),

                  bottomRight: Radius.circular(18.0)

              ),

            ),
          ),
          Padding(padding: EdgeInsets.symmetric(vertical: 8.0,horizontal: 8.0),
            child: Card(
              shape: RoundedRectangleBorder(
                  borderRadius: BorderRadius.circular(16.0)
              ),
              child: Column(
                mainAxisAlignment: MainAxisAlignment.start,
                crossAxisAlignment: CrossAxisAlignment.start,

                children: <Widget>[

                  Text("Amazon Echo Show 8 launched in India: Check out price, features, release date".toUpperCase()

                  ),
                  Text("The company will start shipping the devices from February 26 and it can be pre-booked at the Amazon India website.".toLowerCase(),
                    style: TextStyle(
                        color: Colors.black54
                    ),
                  ),
                  SizedBox(height: 16.0,),
                  Row(
                    children: <Widget>[

                      IconButton(
                        icon: (_isFavorited ? Icon(Icons.favorite) : Icon(
                            Icons.favorite)),
                        color: Color(0xffed1e79),
                        onPressed: _toggleFavorite,
                      ),
                      Text('$_favoriteCount liked'),
                      IconButton(
                        icon: (_isFavorited ? Icon(Icons.favorite_border) : Icon(
                            Icons.favorite_border)),
                        color: Color(0xffed1e79),
                        onPressed: _toggleFavorite,
                      ),
                      Text('17   '),
                      Expanded(child: Text("5 Feb,2020")),
                    ],
                  ),
                  Text("~~~ Reputability score: 0.87")
                ],
              ),
            ),
          ),
          Card(shape: RoundedRectangleBorder(
              borderRadius: BorderRadius.circular(16.0)
          ),
            child: ClipRRect(

              child: Image.network("https://akm-img-a-in.tosshub.com/indiatoday/images/story/202002/RTS30UKV-770x433.jpeg?a2SCUKRPUcPrE5F_dfoq.BOSGwCRblQi"),

              borderRadius: BorderRadius.only(

                  topRight: Radius.circular(18.0),

                  topLeft: Radius.circular(18.0),

                  bottomLeft:Radius.circular(18.0),

                  bottomRight: Radius.circular(18.0)

              ),

            ),
          ),
          Padding(padding: EdgeInsets.symmetric(vertical: 8.0,horizontal: 8.0),
            child: Card(
              shape: RoundedRectangleBorder(
                  borderRadius: BorderRadius.circular(16.0)
              ),
              child: Column(
                mainAxisAlignment: MainAxisAlignment.start,
                crossAxisAlignment: CrossAxisAlignment.start,

                children: <Widget>[

                  Text("Trump snubs Nancy Pelosi, she tears up his speech. Latest viral meme wins Internet over".toUpperCase()

                  ),
                  Text("Trump snubbing Nancy Pelosi and she tearing up his speech has become the latest viral meme on the Internet".toLowerCase(),
                    style: TextStyle(
                        color: Colors.black54
                    ),
                  ),
                  SizedBox(height: 16.0,),
                  Row(
                    children: <Widget>[

                      IconButton(
                        icon: (_isFavorited ? Icon(Icons.favorite) : Icon(
                            Icons.favorite)),
                        color: Color(0xffed1e79),
                        onPressed: _toggleFavorite,
                      ),
                      Text('$_favoriteCount liked'),
                      IconButton(
                        icon: (_isFavorited ? Icon(Icons.favorite_border) : Icon(
                            Icons.favorite_border)),
                        color: Color(0xffed1e79),
                        onPressed: _toggleFavorite,
                      ),
                      Text('17 disliked   '),
                      Expanded(child: Text("5 Feb,2020")),
                    ],
                  ),
                  Text("~~~ Reputability score: 0.87")
                ],
              ),
            ),
          ),
          Card(shape: RoundedRectangleBorder(
              borderRadius: BorderRadius.circular(16.0)
          ),
            child: ClipRRect(

              child: Image.network("https://akm-img-a-in.tosshub.com/indiatoday/images/story/202002/anand-pic-770x433.jpeg?nPXuXBUlF4VQ2YH75CMaJ2F1N76fTdPO"),

              borderRadius: BorderRadius.only(

                  topRight: Radius.circular(18.0),

                  topLeft: Radius.circular(18.0),

                  bottomLeft:Radius.circular(18.0),

                  bottomRight: Radius.circular(18.0)

              ),

            ),
          ),
          Padding(padding: EdgeInsets.symmetric(vertical: 8.0,horizontal: 8.0),
            child: Card(
              shape: RoundedRectangleBorder(
                  borderRadius: BorderRadius.circular(16.0)
              ),
              child: Column(
                mainAxisAlignment: MainAxisAlignment.start,
                crossAxisAlignment: CrossAxisAlignment.start,

                children: <Widget>[

                  Text("Anand Mahindra's new post from his WhatsApp Wonder Box is the best midweek motivation. Internet loves".toUpperCase()

                  ),
                  Text("Anand Mahindra's new post from his WhatsApp Wonder Box is the best midweek motivation you could get today".toLowerCase(),
                    style: TextStyle(
                        color: Colors.black54
                    ),
                  ),
                  SizedBox(height: 16.0,),
                  Row(
                    children: <Widget>[

                      IconButton(
                        icon: (_isFavorited ? Icon(Icons.favorite) : Icon(
                            Icons.favorite)),
                        color: Color(0xffed1e79),
                        onPressed: _toggleFavorite,
                      ),
                      Text('$_favoriteCount liked'),
                      IconButton(
                        icon: (_isFavorited ? Icon(Icons.favorite_border) : Icon(
                            Icons.favorite_border)),
                        color: Color(0xffed1e79),
                        onPressed: _toggleFavorite,
                      ),
                      Text('17 disliked   '),
                      Expanded(child: Text("5 Feb,2020")),
                    ],
                  ),
                  Text("~~~ Reputability score: 0.87")
                ],
              ),
            ),
          ),
          Card(shape: RoundedRectangleBorder(
              borderRadius: BorderRadius.circular(16.0)
          ),
            child: ClipRRect(

              child: Image.network("https://akm-img-a-in.tosshub.com/indiatoday/images/story/202002/imgonline-com-ua-FrameBlurred-_2-770x433.jpeg?c.JiiV8LpQ58dZr7ozErbMuf0_1pDor4"),

              borderRadius: BorderRadius.only(

                  topRight: Radius.circular(18.0),

                  topLeft: Radius.circular(18.0),

                  bottomLeft:Radius.circular(18.0),

                  bottomRight: Radius.circular(18.0)

              ),

            ),
          ),
          Padding(padding: EdgeInsets.symmetric(vertical: 8.0,horizontal: 8.0),
            child: Card(
              shape: RoundedRectangleBorder(
                  borderRadius: BorderRadius.circular(16.0)
              ),
              child: Column(
                mainAxisAlignment: MainAxisAlignment.start,
                crossAxisAlignment: CrossAxisAlignment.start,

                children: <Widget>[

                  Text("China doctor wraps up his wedding in 10 minutes, rushes back to treat coronavirus patients".toUpperCase()

                  ),
                  Text(" A doctor in China had a quick 10-minute wedding so that he can rush back to the hospital and treat the coronavirus patients".toLowerCase(),
                    style: TextStyle(
                        color: Colors.black54
                    ),
                  ),
                  SizedBox(height: 16.0,),
                  Row(
                    children: <Widget>[

                      IconButton(
                        icon: (_isFavorited ? Icon(Icons.favorite) : Icon(
                            Icons.favorite)),
                        color: Color(0xffed1e79),
                        onPressed: _toggleFavorite,
                      ),
                      Text('$_favoriteCount liked'),
                      IconButton(
                        icon: (_isFavorited ? Icon(Icons.favorite_border) : Icon(
                            Icons.favorite_border)),
                        color: Color(0xffed1e79),
                        onPressed: _toggleFavorite,
                      ),
                      Text('17 disliked   '),
                      Expanded(child: Text("5 Feb,2020")),
                    ],
                  ),
                  Text("~~~ Reputability score: 0.87")
                ],
              ),
            ),
          ),
          Card(shape: RoundedRectangleBorder(
              borderRadius: BorderRadius.circular(16.0)
          ),
            child: ClipRRect(

              child: Image.network("nel-patrol-celebrations-occasion-chowk-71st_436fcefa-45a2-11ea-bfa0-35d85fc987f6.jpg"),

              borderRadius: BorderRadius.only(

                  topRight: Radius.circular(18.0),

                  topLeft: Radius.circular(18.0),

                  bottomLeft:Radius.circular(18.0),

                  bottomRight: Radius.circular(18.0)

              ),

            ),
          ),
          Padding(padding: EdgeInsets.symmetric(vertical: 8.0,horizontal: 8.0),
            child: Card(
              shape: RoundedRectangleBorder(
                  borderRadius: BorderRadius.circular(16.0)
              ),
              child: Column(
                mainAxisAlignment: MainAxisAlignment.start,
                crossAxisAlignment: CrossAxisAlignment.start,

                children: <Widget>[

                  Text("Kashmir needs a political outreach".toUpperCase()

                  ),
                  Text(" tics behind it, which would ruin the national harmony.".toLowerCase(),
                    style: TextStyle(
                        color: Colors.black54
                    ),
                  ),
                  SizedBox(height: 16.0,),
                  Row(
                    children: <Widget>[

                      IconButton(
                        icon: (_isFavorited ? Icon(Icons.favorite) : Icon(
                            Icons.favorite)),
                        color: Color(0xffed1e79),
                        onPressed: _toggleFavorite,
                      ),
                      Text('$_favoriteCount liked'),
                      IconButton(
                        icon: (_isFavorited ? Icon(Icons.favorite_border) : Icon(
                            Icons.favorite_border)),
                        color: Color(0xffed1e79),
                        onPressed: _toggleFavorite,
                      ),
                      Text('170 downVote   '),
                      Expanded(child: Text("5 Feb,2020")),
                    ],
                  ),
                  Text("~~~ Reputability score: 0.34")
                ],
              ),
            ),
          ),




        ],
      ),

    );
  }
}
