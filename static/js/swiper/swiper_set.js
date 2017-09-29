$(document).ready(function(){	
 
var swiper = new Swiper('.index_kv .swiper-container', {
        pagination: '.index_kv .swiper-pagination',
        paginationClickable: true,
        nextButton: '.index_kv .swiper-button-next',
        prevButton: '.index_kv .swiper-button-prev',
        slidesPerView: 1,
        spaceBetween: 0,
        speed: 1000,
        loop: true,/*false*/
        autoplay: 7000,/*3000*/
        autoplayDisableOnInteraction: false
    });
    
	    
});