<template>
  <div>
    <div id="header" xmlns="http://www.w3.org/1999/html">
    <div class="mfw-header">
        <div class="header-wrap clearfix" id="_j_head_nav_warper">
            <div class="head-logo"><a class="mfw-logo" title="马蜂窝自由行" href="http://www.mafengwo.cn/"></a></div>
            <ul class="head-nav" data-cs-t="headnav" id="_j_head_nav">
                <li class="head-nav-index _j_head_nav_index head-nav-active" data-cs-p="s" data-tab-item="首页"><a href="http://www.mafengwo.cn/">首页</a></li>
                <li class="head-nav-place _j_head_nav_mdd" data-cs-p="mdd" data-tab-item="目的地"><a href="http://www.mafengwo.cn/mdd/" title="目的地">目的地</a></li>
                <li class="head-nav-gonglve _j_head_nav_gonglve" data-cs-p="gonglve" data-tab-item="旅游攻略"><a href="http://www.mafengwo.cn/gonglve/" title="旅游攻略">旅游攻略</a></li>
                <li class="head-nav-sales _j_head_nav_sales head-nav-dropdown _j_sales_nav_show" id="_j_nav_sales" data-cs-p="sales" data-tab-item="去旅行">
                    <a class="drop-toggle" href="http://www.mafengwo.cn/sales/" style="cursor: pointer;display: block;border-bottom:0 none;" data-sales-nav="去旅行">
                        <span>去旅行<i class="icon-caret-down"></i></span>
                    </a>
                    <div class="dropdown-menu dropdown-sales hide _j_sales_top" id="_j_sales_panel" data-cs-t="sales_nav">
                        <ul>
                            <li><a target="_blank" href="http://localhost:8080/s/" data-sales-nav="自由行">自由行<i class="i-hot">hot</i></a></li>
                            <li><a target="_blank" href="http://www.mafengwo.cn/sales/0-0-0-0-0-0-0-0.html?group=4" data-sales-nav="跟团游">跟团游</a></li>
                            <li><a target="_blank" href="http://www.mafengwo.cn/localdeals/" data-sales-nav="当地游">当地游</a></li>
                            <li><a target="_blank" href="http://www.mafengwo.cn/sales/0-0-0-5-0-0-0-0.html" data-sales-nav="邮轮">邮轮</a></li>
                            <li><a target="_blank" href="http://www.mafengwo.cn/sales/visa/" data-sales-nav="签证">签证</a></li>

                        </ul>
                    </div>
                </li>
                <li class="head-nav-flight _j_head_nav_flight" data-cs-p="flight" data-tab-item="机票"><a href="http://www.mafengwo.cn/flight/" title="国内机票">机票</a></li>
                <li class="head-nav-hotel _j_head_nav_hotel" data-cs-p="hotel" data-tab-item="酒店"><a href="http://www.mafengwo.cn/hotel/" title="酒店">订酒店</a></li>
                <li class="head-nav-community _j_head_nav_community head-nav-dropdown _j_shequ_nav_show" id="_j_nav_community" data-cs-p="community" data-tab-item="社区">
                    <div class="drop-toggle"><span>社区<i class="icon-caret-down"></i></span></div>
                    <!-- 社区下拉面板 begin -->
                    <div class="dropdown-panel dropdown-community hide _j_shequ_top no-image" id="_j_community_panel" data-cs-t="community_nav">
                        <div class="panel-wrapper">
                            <ul class="nav-list clearfix">
                                <li class="h"><a href="http://www.mafengwo.cn/wenda/" target="_blank" title="问答" data-cs-p="wenda">问答<i class="i-hot">hot</i></a></li>
                                <li><a href="http://www.mafengwo.cn/mall/things.php" target="_blank" title="马蜂窝周边" data-cs-p="things">马蜂窝周边<i class="i-new">new</i></a></li>
                                <li><a href="http://www.mafengwo.cn/club/" target="_blank" title="蜂首俱乐部" data-cs-p="club">蜂首俱乐部</a></li>
                                <li><a href="http://www.mafengwo.cn/together/" target="_blank" title="结伴" data-cs-p="together">结伴</a></li>
                            </ul>
                            <ul class="nav-list-sub clearfix">

                                <li><a href="http://www.mafengwo.cn/group/" target="_blank" title="马蜂窝旅行家" data-cs-p="group">小组论坛</a></li>
                                <li><a href="http://www.mafengwo.cn/rudder/" target="_blank" title="分舵同城" data-cs-p="rudder">分舵同城</a></li>
                                <li><a href="http://www.mafengwo.cn/auction/" target="_blank" title="马蜂窝拍卖行" data-cs-p="paimai">马蜂窝拍卖行</a></li>

                                <!--<li><a href="http://www.mafengwo.cn/postal/" target="_blank" title="游记纪念工厂" data-cs-p="postal">游记纪念工厂</a></li>-->
                                <li><a href="http://www.mafengwo.cn/photo_pk/prev.php" target="_blank" title="照片PK" data-cs-p="photo_pk">照片PK</a></li>
                                <li><a href="http://www.mafengwo.cn/focus/" target="_blank" title="真人兽" data-cs-p="focus">真人兽</a></li>
                                <li><a href="http://www.mafengwo.cn/mall/virtual_goods.php" target="_blank" title="道具商店" data-cs-p="virtual">道具商店</a></li>
                            </ul>
                        </div>
                    </div>

                    <!-- 社区下拉面板 end -->
                </li>
                <li class="head-nav-app _j_head_nav_app" data-cs-p="app" data-tab-item="APP"><a href="http://www.mafengwo.cn/app/intro/gonglve.php" title="APP">APP</a></li>
                <li class="head-nav-choice _j_head_nav_choice" data-cs-p="choice" data-tab-item="马蜂窝旅行者之选"><a href="http://www.mafengwo.cn/poi/choice/group"><div class="mfwzx-logo"></div></a></li>
            </ul>
            <div class="head-search" data-online="1">
                <div class="head-search-wrapper">
                    <div class="head-searchform">
                        <input name="q" type="text" id="_j_head_search_input" autocomplete="off">
                        <a role="button" href="javascript:" class="icon-search" id="_j_head_search_link"></a>
                    </div>
                </div>
            </div>
            <div id="pagelet-block-159051b6ca00900bc6cb7ec08172705c" class="pagelet-block" data-api="apps:user:pagelet:pageViewHeadInfo" data-params="{&quot;type&quot;:1}" data-async="1" data-controller="/js/pageletcommon/pageHeadUserInfoWWWNormal">	<div class="login-out">
		<a class="weibo-login" href="https://passport.mafengwo.cn/weibo" title="微博登录" rel="nofollow"></a>
		<a class="qq-login" href="https://passport.mafengwo.cn/qq" title="QQ登录" rel="nofollow"></a>
		<a class="weixin-login" href="https://passport.mafengwo.cn/wechat" title="微信登录" rel="nofollow"></a>
		<a id="_j_showlogin" title="登录马蜂窝" href="https://passport.mafengwo.cn" rel="nofollow">登录</a><span class="split">|</span><a href="https://passport.mafengwo.cn/regist.html" title="注册帐号" rel="nofollow">注册</a>
	</div>
</div>
        </div>
        <div class="shadow"></div>
    </div>

    <!-- 新自由行菜单 begin -->
<div class="dropdown-bar" style="display: none">
    <div class="content">
        <ul class="clearfix ul-dropdown-bar" id="Js_middleNav">
            <li data-type="sales"><a href="http://www.mafengwo.cn/sales/">自由行</a></li>
            <li data-type="freewalker"><a href="http://www.mafengwo.cn/sales/0-0-0-0-0-0-0-0.html?group=4">跟团游</a></li>
            <li data-type="localdeals"><a href="http://www.mafengwo.cn/localdeals/">当地游</a></li>

            <li data-type="visa"><a href="http://www.mafengwo.cn/sales/visa/">签证</a></li>
            <li data-type="wifi"><a href="http://www.mafengwo.cn/localdeals/0-0-0-21-0-0-0-0.html">全球WiFi</a></li>
            <li data-type="cruise"><a href="http://www.mafengwo.cn/sales/0-0-0-5-0-0-0-0.html">邮轮</a></li>


        </ul>
    </div>

</div>
<!-- 新自由行菜单 end -->

</div>
  </div>
</template>
