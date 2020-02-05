var express = require('express');
var mysql = require('mysql');
var app = express();
var handlebars = require('express-handlebars').create({defaultLayout:'main'});
var bodyParser = require('body-parser');

app.use(express.static('public'));
app.use(bodyParser.urlencoded({ extended: false }));
app.use(bodyParser.json());

var pool = mysql.createPool({
    host  : 'xxxx',
    user  : 'xxxx',
    password: 'xxxx',
    database: 'xxxx'
});


app.engine('handlebars', handlebars.engine);
app.set('view engine', 'handlebars');
app.set('port', 4499);
app.use(express.static('public'));


app.get('/',function(req,res,next){
    var context = {};
    pool.query('SELECT * FROM articles', function(err, rows, fields){
        if(err){
            next(err);
            return;
        }
        context.results = JSON.stringify(rows);
        var articles = [];
        for  (var row in rows)
        {
            articles.push(rows[row]);
        }
        context.articles = articles;
        res.render('articles', context);
    });
});


app.get('/insert-link',function(req,res,next){
    var context = {};
    pool.query("INSERT INTO articles (`link`) VALUES (?)",  [req.query.link], function(err, rows, fields){
        if(err){
            next(err);
            return;
        }
        context.results = JSON.stringify(rows);
        res.send(context.results);
    });
});


app.get('/get-unverified-count',function(req,res,next){
    var context = {};
    pool.query("SELECT unverified FROM articles WHERE link=?",  [req.query.link], function(err, rows, fields){
        if(err){
            next(err);
            return;
        }
        context.results = JSON.stringify(rows);
        res.send(context.results);
    });
});


app.get('/get-verified-count',function(req,res,next){
    console.log(req.query);
    var context = {};
    pool.query("SELECT verified FROM articles WHERE link=?",  [req.query.link], function(err, rows, fields){
        if(err){
            next(err);
            return;
        }
        context.results = JSON.stringify(rows);
        res.send(context.results);
    });
});


app.get('/update-unverified-count',function(req,res,next){
    var context = {};
    pool.query("UPDATE articles SET unverified=? WHERE link=?",  [req.query.unverified, req.query.link], function(err, rows, fields){
        if(err){
            next(err);
            return;
        }
        context.results = JSON.stringify(rows);
        res.send(context.results);
    });
});


app.get('/update-verified-count',function(req,res,next){
    console.log(req.query);
    var context = {};
    pool.query("UPDATE articles SET verified=? WHERE link=?",  [req.query.verified, req.query.link], function(err, rows, fields){
        if(err){
            next(err);
            return;
        }
        context.results = JSON.stringify(rows);
        res.send(context.results);
        console.log(context.results);
    });
});


app.get('/get-fields',function(req,res,next){
    var context = {};
    pool.query("SELECT articleID, link, verified, unverified, rate FROM articles WHERE link=?",  [req.query.link], function(err, rows, fields){
        if(err){
            next(err);
            return;
        }
        context.results = JSON.stringify(rows);
        res.send(context.results);
    });
});


app.get('/article-found',function(req,res,next){
    var context = {};
    pool.query("SELECT link FROM articles WHERE link=?",  [req.query.link], function(err, rows, fields){
        if(err){
            next(err);
            return;
        }
        context.results = JSON.stringify(rows);
        console.log(context.results);
        res.send(context.results);
    });
});

app.post('/',function(req,res){
    var post = {link:req.body.link};
    
    pool.query("INSERT INTO articles SET ?", post, function(err, result){
        if(err){
            next(err);
            return;
        }
        res.redirect('/');
    });
});


app.use(function(req,res){
    res.status(404);
    res.render('404');
});

app.use(function(err, req, res, next){
    console.error(err.stack);
    res.status(500);
    res.render('500');
});

app.listen(app.get('port'), function(){
    console.log('Express started on http://localhost:' + app.get('port') + '; press Ctrl-C to terminate.');
});
