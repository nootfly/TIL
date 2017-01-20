# mongojs aggregate

This example is to aggregate records with the same `memberId` and date. The return json group filed name must `_id`.

   ```javascript
   var findQuery = {memberId:req.params.id};
    mongodb.tierPoints.aggregate([
    { $match: findQuery },
     {$group: { _id: {  $substr: ["$updateDate",0, 10]  }
     , total: { $sum: "$changeAmount" }
     }} ],function(err, points){
        if(err){
            res.send(err);
        }
        res.json(points);
    });
   ```
