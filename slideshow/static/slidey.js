var g_show_frame;
var g_show_data;
var g_current_item = -1;

function run_show() {
    g_current_item = (g_current_item + 1) % g_show_data.length;

    var dest = g_show_data[g_current_item]['fields']['url'];
    if (g_show_data[g_current_item]['fields']['mode'] != null) {
        dest = '/slideshow/transform/' +
            g_show_data[g_current_item]['pk'] + '/';
    }

    g_show_frame.location.href = dest;
    setTimeout('run_show()',
               1000 * g_show_data[g_current_item]['fields']['display_duration']);
}