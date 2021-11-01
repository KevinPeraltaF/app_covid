(function(a){a.fn.extend({slimScroll:function(d){var b={width:"auto",height:"250px",size:"7px",color:"#000",position:"right",distance:"1px",start:"top",opacity:0.4,alwaysVisible:false,disableFadeOut:false,railVisible:false,railColor:"#333",railOpacity:0.2,railDraggable:true,railClass:"slimScrollRail",barClass:"slimScrollBar",wrapperClass:"slimScrollDiv",allowPageScroll:false,wheelStep:20,touchScrollStep:200,borderRadius:"7px",railBorderRadius:"7px"};var c=a.extend(b,d);this.each(function(){var q,p,o,y,D,i,w,r,j="<div></div>",u=30,A=false;var s=a(this);if(s.parent().hasClass(c.wrapperClass)){var v=s.scrollTop();g=s.siblings("."+c.barClass);z=s.siblings("."+c.railClass);k();if(a.isPlainObject(d)){if("height" in d&&d.height=="auto"){s.parent().css("height","auto");s.css("height","auto");var m=s.parent().parent().height();s.parent().css("height",m);s.css("height",m)}else{if("height" in d){var l=d.height;s.parent().css("height",l);s.css("height",l)}}if("scrollTo" in d){v=parseInt(c.scrollTo)}else{if("scrollBy" in d){v+=parseInt(c.scrollBy)}else{if("destroy" in d){g.remove();z.remove();s.unwrap();return}}}B(v,false,true)}return}else{if(a.isPlainObject(d)){if("destroy" in d){return}}}c.height=(c.height=="auto")?s.parent().height():c.height;var E=a(j).addClass(c.wrapperClass).css({position:"relative",overflow:"hidden",width:c.width,height:c.height});s.css({overflow:"hidden",width:c.width,height:c.height});var z=a(j).addClass(c.railClass).css({width:c.size,height:"100%",position:"absolute",top:0,display:(c.alwaysVisible&&c.railVisible)?"block":"none","border-radius":c.railBorderRadius,background:c.railColor,opacity:c.railOpacity,zIndex:90});var g=a(j).addClass(c.barClass).css({background:c.color,width:c.size,position:"absolute",top:0,opacity:c.opacity,display:c.alwaysVisible?"block":"none","border-radius":c.borderRadius,BorderRadius:c.borderRadius,MozBorderRadius:c.borderRadius,WebkitBorderRadius:c.borderRadius,zIndex:99});var x=(c.position=="right")?{right:c.distance}:{left:c.distance};z.css(x);g.css(x);s.wrap(E);s.parent().append(g);s.parent().append(z);if(c.railDraggable){g.bind("mousedown",function(F){var h=a(document);o=true;t=parseFloat(g.css("top"));pageY=F.pageY;h.bind("mousemove.slimscroll",function(G){currTop=t+G.pageY-pageY;g.css("top",currTop);B(0,g.position().top,false)});h.bind("mouseup.slimscroll",function(G){o=false;n();h.unbind(".slimscroll")});return false}).bind("selectstart.slimscroll",function(h){h.stopPropagation();h.preventDefault();return false})}z.hover(function(){C()},function(){n()});g.hover(function(){p=true},function(){p=false});s.hover(function(){q=true;C();n()},function(){q=false;n()});s.bind("touchstart",function(F,h){if(F.originalEvent.touches.length){D=F.originalEvent.touches[0].pageY}});s.bind("touchmove",function(F){if(!A){F.originalEvent.preventDefault()}if(F.originalEvent.touches.length){var h=(D-F.originalEvent.touches[0].pageY)/c.touchScrollStep;B(h,true);D=F.originalEvent.touches[0].pageY}});k();if(c.start==="bottom"){g.css({top:s.outerHeight()-g.outerHeight()});B(0,true)}else{if(c.start!=="top"){B(a(c.start).position().top,null,true);if(!c.alwaysVisible){g.hide()}}}f(this);function e(F){if(!q){return}var F=F||window.event;var h=0;if(F.wheelDelta){h=-F.wheelDelta/120}if(F.detail){h=F.detail/3}var G=F.target||F.srcTarget||F.srcElement;if(a(G).closest("."+c.wrapperClass).is(s.parent())){B(h,true)}if(F.preventDefault&&!A){F.preventDefault()}if(!A){F.returnValue=false}}function B(J,G,F){A=false;var h=J;var H=s.outerHeight()-g.outerHeight();if(G){h=parseInt(g.css("top"))+J*parseInt(c.wheelStep)/100*g.outerHeight();h=Math.min(Math.max(h,0),H);h=(J>0)?Math.ceil(h):Math.floor(h);g.css({top:h+"px"})}w=parseInt(g.css("top"))/(s.outerHeight()-g.outerHeight());h=w*(s[0].scrollHeight-s.outerHeight());if(F){h=J;var I=h/s[0].scrollHeight*s.outerHeight();I=Math.min(Math.max(I,0),H);g.css({top:I+"px"})}s.scrollTop(h);s.trigger("slimscrolling",~~h);C();n()}function f(h){if(window.addEventListener){h.addEventListener("DOMMouseScroll",e,false);h.addEventListener("mousewheel",e,false)}else{document.attachEvent("onmousewheel",e)}}function k(){i=Math.max((s.outerHeight()/s[0].scrollHeight)*s.outerHeight(),u);g.css({height:i+"px"});var h=i==s.outerHeight()?"none":"block";g.css({display:h})}function C(){k();clearTimeout(y);if(w==~~w){A=c.allowPageScroll;if(r!=w){var h=(~~w==0)?"top":"bottom";s.trigger("slimscroll",h)}}else{A=false}r=w;if(i>=s.outerHeight()){A=true;return}g.stop(true,true).fadeIn("fast");if(c.railVisible){z.stop(true,true).fadeIn("fast")}}function n(){if(!c.alwaysVisible){y=setTimeout(function(){if(!(c.disableFadeOut&&q)&&!p&&!o){g.fadeOut("slow");z.fadeOut("slow")}},1000)}}});return this}});a.fn.extend({slimscroll:a.fn.slimScroll})})(jQuery);