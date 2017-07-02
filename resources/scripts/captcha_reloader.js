$(document).ready(function(){
					function captcha_new(){
                            $("#captcha_img").attr("src", "/captcha?q=" + 
                                                   Math.random());
                        } 
                        
                        $("#captcha_new").click(captcha_new);
                    });