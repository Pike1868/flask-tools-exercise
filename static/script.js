window.onload = function check_for_flash_messages() {
  let $flash_msg = $(".flash_msg");
  console.log($flash_msg);
  let $main_content = $("main");
  $main_content.hide();

  setTimeout(() => {
    $main_content.show();
    flash_msg.remove();
  }, 1000);
};
