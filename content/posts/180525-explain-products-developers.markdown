title: How to Explain Your Products to Developers
slug: explain-products-developers
meta: Talk slides, notes and more resources for a technical talk on developer marketing for tech products, by Matt Makai.
category: talk
date: 2018-05-25
modified: 2018-05-25
newsletter: False
headerimage: /img/180526-explain-product/01-explain-products.jpg
headeralt: Comment bubble with code representing a technical talk-based blog post.


This blog post contains the slides along with a loose transcript
from my talk on appropriately marketing products to 
software developers that I gave at
[Silicon Valley Bank](https://www.svb.com/) during 
[Ubiquity.VC](http://www.ubiquity.vc/)'s summit for founders, investors and 
technical advisors on May 24, 2018.

----

<div class="row talk"><div class="c6">
<img src="/img/180526-explain-product/01-explain-products.jpg" width="100%" class="shot rnd outl" alt="Title slide for this talk on Explaining Products to Developers.">
</div><div class="c6"><p>
Hey folks, my name is <a href="/about-author.html">Matt Makai</a>. I serve the
<a href="https://www.youtube.com/watch?v=TF129ioe8kc">Developer Network</a> at
<a href="https://www.twilio.com/">Twilio</a>. We've talked a lot today about 
making the real, physical world programmable. We ask "what if we could modify 
the world using GitHub and Jira?" When we succeed in creating programmatic 
access to the physical world, what then? Is that the end goal?
</p><p>
No, that's only the beginning. We need developers to use those new 
capabilities and code with them. 
</p><p>
How do you get developers to adopt what you are creating? That is a broad 
question so I am going to zoom in on just one small slice of developer 
relations that kicks off the whole adoption process. Unfortunately I 
see upwards of 90% of companies completely screw up explaining their 
products to developers.
</p><p>
Today we are going to look at how to appropriately explain and demo your 
product to developers to maximize developer adoption. This is the first
step towards getting a developer to care enough to try out what you have 
built.
</p></div></div>


<div class="row talk"><div class="c6">
<img src="/img/180526-explain-product/02-matt-makai-bio.jpg" width="100%" class="shot rnd outl" alt="Bio information slide for Matt Makai.">
</div><div class="c6"><p>
In addition to serving the Developer Network at Twilio, I am also a 
<a href="https://www.python.org/">Python</a> and 
<a href="https://swift.org/">Swift</a> developer as well as the creator of 
<a href="https://www.fullstackpython.com/">Full Stack Python</a>. My 
background provides me an opportunity to give insight on this topic because 
I am a software developer, I market to fellow software developers and I write a 
community-driven site that is widely read and trusted by software developers.
</p></div></div>


<div class="row talk"><div class="c6">
<img src="/img/180526-explain-product/03-show-it-live.jpg" width="100%" class="shot rnd outl" alt="Fred Wilson quote on showing rather than telling.">
</div><div class="c6"><p>
How do you explain your product? <a href="https://avc.com/">Fred Wilson</a> 
of <a href="https://www.usv.com/">Union Square Ventures</a> said it best in 
this quote, which we will roughly summarize as: 
<em>show, don't just tell</em>.
</p></div></div>


<div class="row talk"><div class="c6">
<img src="/img/180526-explain-product/04-demo.jpg" width="100%" class="shot rnd outl" alt="Demo slide for transitioning into a live-coded demo.">
</div><div class="c6"><p>
With Fred Wilson's quote in mind, it's demo time! 
</p><p>
(This is where I do a condensed, approximately two minute version of my 
Twilio five minute live-coded demo. For a rough approximation of what I 
showed, check out the 
<a href="https://www.youtube.com/watch?v=-VuXIgp9S7o">NY Tech Meetup Twilio demo</a>
from 2010.)
</p></div></div>


<div class="row talk"><div class="c6">
<img src="/img/180526-explain-product/05-phone-api.jpg" width="100%" class="shot rnd outl" alt="Twilio 2008-2011 had only the phone calling voice API.">
</div><div class="c6"><p>
That demo represented the Twilio 5 minute demo from 2008 through part of 
2011, when the 
<a href="https://www.twilio.com/docs/voice/api">phone calling voice API</a> 
was the company's main product.
</p></div></div>


<div class="row talk"><div class="c6">
<img src="/img/180526-explain-product/06-story-arc.jpg" width="100%" class="shot rnd outl" alt="Story arc visual.">
</div><div class="c6"><p>
Let's break down the demo into its component pieces so we can learn from
it. The demo narrative fits into a story arc. Yes, a story arc like from a
novel. You may not have thought about explaining and showing your product
in a couple of minutes to be similiar to a novel, but you should follow the 
same narrative structure because it is easier for the audience to understand.
<p></p>
The demo we just saw follows the story arc in the beginning when I introduce 
myself and Twilio. A clear, concise set of intentional words are used to 
explain what Twilio *can do for a developer*. "Twilio makes it easy for 
software developers to add phone calling to applications using the 
programming languages that you already know." Breaking that down further:
</p>
<ol>
<li><strong>software developers</strong>: a clear call out to who we are 
talking to</li>
<li><strong>phone calling</strong>: what problem we solve by adding this 
feature to applications</li>
<li><strong>programming languages that you already know</strong>: emphasizing
that you do not have to learn some complicated proprietary syntax from the 
telecommunications world</li>
</ol>
<p>
Next in the exposition, we explain how it works 
<a href="https://s3.amazonaws.com/com.twilio.prod.twilio-docs/images/incoming-voice.width-800.png">using a diagram</a>
that shows inbound and outbound phone calls and how they interact with 
Twilio's service as well as your <a href="/web-servers.html">web server</a>.
</p><p>
The inciting incident during the demo  happens when I finish the 
explanation of how Twilio works and say "rather than just show you a
little diagram, let's build an application together right now".
</p><p>
We move into the demo phase where I buy and configure a phone number then
we all test it by calling the number on our own cell phones. The audience 
learns that to configure the phone number to do something useful in this
case only requires two XML elements that can be stored in a static file or 
generated by an endpoint in their application.
</p><p>
The climax hits when we see outbound phone calling, everyone's
phones in the room start ringing and we are all on speaker phone together.
Finally, there is a short resolution where I re-explain what Twilio can
do for developers and outro with my name and where you can find me.
</p><p>
The whole two minute demo, or however long we need it to be, has a narrative
with a clear story arc.
</p></div></div>


<div class="row talk"><div class="c6">
<img src="/img/180526-explain-product/07-sms-2011.jpg" width="100%" class="shot rnd outl" alt="Twilio added an SMS API in 2011.">
</div><div class="c6"><p>
In 2011, Twilio added SMS. This changed the 5 minute demo's explanation
to "Twilio makes it easy for developers to send and receive text messages
and make and receive phone calls using the programming languages that they
already know". The overall structure otherwise remained the same because we 
used SMS for inbound action and kept phone calling for the outbound action. 
</p><p>
Eventually your product line or features within a product line will reach
a point where you need to determine if it changes your explanation and
demo. In some cases there will be modifications that fit within the existing
framework and do not substantially change the narrative.
</p></div></div>

<div class="row talk"><div class="c6">
<img src="/img/180526-explain-product/08-more-products.jpg" width="100%" class="shot rnd outl" alt="Eventually you expand your product lines or features within a product.">
</div><div class="c6"><p>
As you continue to grow you will eventually reach an inflection point where
you have too many products or features to explain, regardless of how
much time you have for your demo. You reach a situation where if you try to 
tell the audience everything that your product does, they will zone out
and ignore your laundry list of features.
</p><p>
If you are not intentional in the words you say and specific
in the products and features you choose to show, then your pitch becomes 
spread too thin and no developer will care to listen.
</p><p>
Twilio now has dozens of products under the communications umbrella. I talk
about specific products and tailor my explanation based on the audience. You
should too! For example, if I am talking to a group of web developers, I will
still use the classic Twilio 5 minute demo that shows off SMS and phone 
calling capability. On the other hand, if I am demoing to iOS and Android 
mobile developers then I will show off 
<a href="https://www.twilio.com/docs/chat">Programmable Chat</a> or 
<a href="https://www.twilio.com/docs/video">Programmable Video</a>.
</p><p>
The explanation is tuned to "Twilio makes it easy for developers to add 
communications, such as phone calling, messaging and video, to their 
applications using the programming languages that they already know." I 
draw a broad theme by saying the word "communications" then give three
specific examples of products that are the most widely used by developers
because they are incredibly useful for implementing common application
features.
</p></div></div>


<div class="row talk"><div class="c6">
<img src="/img/180526-explain-product/09-devangelism.jpg" width="100%" class="shot rnd outl" alt="You as a founder, or as an investor who work with founders must be the chief evangelist for your product.">
</div><div class="c6"><p>
It's time to reinforce why it is so important for you, as a founder, or as an
investor that works with founders, to be the chief evangelist for your
product. You cannot ever outsource this role. You cannot hire someone to
lead an evangelism team and expect them to figure it all out for you. 
</p><p>
If you are not excited about the product you are building or are unable 
to transfer that excitement to developers with a clear explanation and demo, 
then all of the other priorities for your company become useless. If 
developers are your customers and they do not adopt your product then you
will not sell anything, you won't be able to set a great company culture
and you won't need to worry about what snacks are stocked in your office's
kitchen. If developers are the lifeblood of your company then you need to
be the chief evangelist, period.
</p><p>
Here are a few more important points for how to perform this role 
effectively.
</p></div></div>


<div class="row talk"><div class="c6">
<img src="/img/180526-explain-product/10-be-specific.jpg" width="100%" class="shot rnd outl" alt="The earlier you are, the more specific you need to be about what problem you solve.">
</div><div class="c6"><p>
When you are early stage, be as specific as possible about what problem
that you are solving. You are <strong>not</strong> "disrupting 
transportation by blah blah blah". No developer gives a shit. They want to 
know what problem you will solve for them right now.
</p><p>
Be specific, like the "add phone calling to your applications" line so that
it is absolutely clear what you do.
</p><p>
When your company grows and your brand expands, then you may expand to 
include the general industry your company works in, such as "communications".
Do not jump the gun in trying to become too grandiose with your ambitions 
because your developer audience cares about what problem you are solving for
them, not who you imagine yourself to be in your future vision.
</p></div></div>


<div class="row talk"><div class="c6">
<img src="/img/180526-explain-product/11-refine-growth.jpg" width="100%" class="shot rnd outl" alt="Refine the message as you grow, or your industry grows.">
</div><div class="c6"><p>
Refine the explanation you use and the demo under two situations. 
</p><p>
First, when your products and features expand. Think critically if a new 
feature should be part of your explanation or it can be left as an answer 
to follow up questions that a developer asks you. 
</p><p>
Second, developer ecosystems are constantly changing. If you tried to talk
to me about containers ten years ago and I was not a Solaris sysadmin then
I would not have any clue what you are talking about. Today, it's generally
safe to assume most Bay Area developers have a working knowledge of what
containers are and what they are useful for accomplishing. Use that type of
context in your pitch to reinforce your technical credibility with your
developer audience.
</p></div></div>


<div class="row talk"><div class="c6">
<img src="/img/180526-explain-product/12-rehearsal.jpg" width="100%" class="shot rnd outl" alt="No demo fails because you rehearse constantly.">
</div><div class="c6"><p>
I get asked a lot about live coding because everyone is worried about demo
fails. You should not demo fail, ever. To steal a line from 
<a href="https://github.com/RobSpectre">Rob Spectre</a>, former head of the 
Twilio Developer Network:</p>

<blockquote>There is only one demo God, and her name is rehearsal.</blockquote>

<p>
You do not just rehearse and practice the happy path, you also practice
what can go wrong. What happens when you mistype a character in your code?
Find out and get used to it. If and when it happens during your live demo 
then you can incorporate that mistake into your narrative as a learning
opportunity for the audience.
</p><p>
Magicians always have "outs" in their acts, essentially plan B, plan C, 
plan Z. You should too because something will always go wrong but if you
are ready for it and know how to handle it then you will never demo fail.
</p></div></div>


<div class="row talk"><div class="c6">
<img src="/img/180526-explain-product/13-your-message-to-devs.jpg" width="100%" class="shot rnd outl" alt="Your message to developers.">
</div><div class="c6"><p>
That sums up my strong recommendations for this one small slice of the
field of developer product adoption. To re-iterate, create a narrative 
for your explanation and demo that follows the classic story arc. The 
earlier you are as a product, the more specific your explanation should
be in what problem you solve. Refine the message as your features and
product lines grow, as well as when the industry around you changes. 
Rehearse your demo including what can and will go wrong.
</p><p>
There is a lot more to developer adoption than a good explanation and
demo, but I see greater than 90% of companies never even get to this
point so you will be way ahead of the pack if you heed the advice from
this talk.
</p></div></div>


<div class="row talk"><div class="c6">
<img src="/img/180526-explain-product/14-thank-you.jpg" width="100%" class="shot rnd outl" alt="Thank you slide.">
</div><div class="c6"><p>
That's all for today. My name is <a href="/about-author.html">Matt Makai</a>,
I am a software developer at <a href="/twilio.html">Twilio</a> and the
author of <a href="https://www.fullstackpython.com/">Full Stack Python</a>.
Thank you very much.
</p></div></div>
