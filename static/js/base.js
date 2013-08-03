  $('.affix').affix({
    offset: {
      top: function(){
      	return $("#landing-header").height();
      }
    }
  });

  