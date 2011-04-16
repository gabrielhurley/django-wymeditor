(function ($) {
    $(function () {
        wymeditor_filebrowser = function(wym, wdw) {
            // Django filebrowser URL, #FIXME -- depends on URLconf
            var fb_url = '/admin/filebrowser/browse/',
                dlg = $(wdw.document.body);

            if (dlg.hasClass('wym_dialog_image')) {
                // this is an image dialog
                dlg.find('.wym_src')
                    .css('width', '200px')
                    .attr('id', 'filebrowser')
                    .after('<a id="fb_link" title="Filebrowser" href="#">Filebrowser</a>');
                dlg.find('fieldset')
                    .append('<a id="link_filebrowser"><img id="image_filebrowser" /></a>'
                            + '<br /><span id="help_filebrowser"></span>');
                dlg.find('#fb_link').click(function() {
                    fb_window = wdw.open(
                        fb_url + '?pop=1',
                        'filebrowser',
                        'height=600,width=840,resizable=yes,scrollbars=yes'
                    );
                    fb_window.focus();
                    return false;
                });
          }
        }

        $(".WYMEditor").wymeditor({
            updateSelector: "input:submit",
            updateEvent: "click",
            postInitDialog: wymeditor_filebrowser,
            logoHtml: '',
            skin: 'twopanels',
            classesItems: [
                {'name': 'image', 'title': 'DIV: Image w/ Caption', 'expr': 'div'},
                {'name': 'caption', 'title': 'P: Caption', 'expr': 'p'},
                {'name': 'align-left', 'title': 'Float: Left', 'expr': 'p, div, img'},
                {'name': 'align-right', 'title': 'Float: Right', 'expr': 'p, div, img'}
            ]
        });
    });
})(jQuery);