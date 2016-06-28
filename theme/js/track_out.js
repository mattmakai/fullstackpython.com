var trackOutboundLink = function(url) {
   ga('send', 'event', 'outbound', 'click', url, {'hitCallback':
     function () { document.location = url; } }); }
