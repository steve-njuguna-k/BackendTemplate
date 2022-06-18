ICON_DIMENSIONS = 'width="14px" height="14px"'
COLOR = "white"
ICON_COLOR = f'style="fill: {COLOR}"'

user_label_with_icon = (
    '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 448 512" '
    + f'{ICON_DIMENSIONS}><path d="M224 256c70.7 0 128-57.31 128-128s-57.3-128-'
    + "128-128C153.3 0 96 57.31 96 128S153.3 256 224 256zM274.7 304H173.3C77.61"
    + " 304 0 381.6 0 477.3c0 19.14 15.52 34.67 34.66 34.67h378.7C432.5 512 448"
    + f' 496.5 448 477.3C448 381.6 370.4 304 274.7 304z"{ICON_COLOR}/></svg>&n'
    + "bsp;&nbsp;&nbsp;Users"
)

profile_label_with_icon = (
    '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 576 512"'
    + f'{ICON_DIMENSIONS}><path d="M512 32H64C28.65 32 0 60.65 0 96v320c0 35.35'
    + " 28.65 64 64 64h448c35.35 0 64-28.65 64-64V96C576 60.65 547.3 32 512 32z"
    + "M176 128c35.35 0 64 28.65 64 64s-28.65 64-64 64s-64-28.65-64-64S140.7 12"
    + "8 176 128zM272 384h-192C71.16 384 64 376.8 64 368C64 323.8 99.82 288 144"
    + " 288h64c44.18 0 80 35.82 80 80C288 376.8 280.8 384 272 384zM496 320h-128"
    + "C359.2 320 352 312.8 352 304S359.2 288 368 288h128C504.8 288 512 295.2 5"
    + "12 304S504.8 320 496 320zM496 256h-128C359.2 256 352 248.8 352 240S359.2"
    + " 224 368 224h128C504.8 224 512 231.2 512 240S504.8 256 496 256zM496 192h"
    + "-128C359.2 192 352 184.8 352 176S359.2 160 368 160h128C504.8 160 512 167"
    + f'.2 512 176S504.8 192 496 192z"{ICON_COLOR}/></svg>&nbsp;&nbsp;&nbsp;'
    + "Profiles"
)

suggestion_label_with_icon = (
    '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 512 512"'
    + f'{ICON_DIMENSIONS}><path d="M256 32C114.6 32 .0272 125.1 .0272 240c0 49.'
    + "63 21.35 94.98 56.97 130.7c-12.5 50.37-54.27 95.27-54.77 95.77c-2.25 2.2"
    + "5-2.875 5.734-1.5 8.734C1.979 478.2 4.75 480 8 480c66.25 0 115.1-31.76 1"
    + "40.6-51.39C181.2 440.9 217.6 448 256 448c141.4 0 255.1-93.13 255.1-208S3"
    + f'97.4 32 256 32z"{ICON_COLOR}/></svg>&nbsp;&nbsp;&nbsp;Suggestions'
)

email_label_with_icon = (
    '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 512 512"'
    + f'{ICON_DIMENSIONS}><path d="M464 64C490.5 64 512 85.49 512 112C512 127.1'
    + " 504.9 141.3 492.8 150.4L275.2 313.6C263.8 322.1 248.2 322.1 236.8 313.6"
    + "L19.2 150.4C7.113 141.3 0 127.1 0 112C0 85.49 21.49 64 48 64H464zM217.6 "
    + "339.2C240.4 356.3 271.6 356.3 294.4 339.2L512 176V384C512 419.3 483.3 44"
    + f'8 448 448H64C28.65 448 0 419.3 0 384V176L217.6 339.2z"{ICON_COLOR}/></s'
    + "vg>&nbsp;&nbsp;&nbsp;Emails"
)

block_label_with_icon = (
    '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 512 512" '
    + f' {ICON_DIMENSIONS}><path d="M256 417.1c-16.38 0-32.88-4.1-46.88-1'
    + "5.12L0 250.9v213.1C0 490.5 21.5 512 48 512h416c26.5 0 48-21.5 48-47.1V25"
    + "0.9l-209.1 151.1C288.9 412 272.4 417.1 256 417.1zM493.6 163C484.8 156 47"
    + "6.4 149.5 464 140.1v-44.12c0-26.5-21.5-48-48-48l-77.5 .0016c-3.125-2.25-"
    + "5.875-4.25-9.125-6.5C312.6 29.13 279.3-.3732 256 .0018C232.8-.3732 199.4"
    + " 29.13 182.6 41.5c-3.25 2.25-6 4.25-9.125 6.5L96 48c-26.5 0-48 21.5-48 4"
    + "8v44.12C35.63 149.5 27.25 156 18.38 163C6.75 172 0 186 0 200.8v10.62l96 "
    + "69.37V96h320v184.7l96-69.37V200.8C512 186 505.3 172 493.6 163zM176 255.1"
    + "h160c8.836 0 16-7.164 16-15.1c0-8.838-7.164-16-16-16h-160c-8.836 0-16 7."
    + "162-16 16C160 248.8 167.2 255.1 176 255.1zM176 191.1h160c8.836 0 16-7.16"
    + "4 16-16c0-8.838-7.164-15.1-16-15.1h-160c-8.836 0-16 7.162-16 15.1C160 18"
    + f'4.8 167.2 191.1 176 191.1z"{ICON_COLOR}/></svg>&nbsp;&nbsp;&nbsp;Blocks'
)

log_label_with_icon = (
    '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 512 512"'
    + f' {ICON_DIMENSIONS}><path d="M256 0C397.4 0 512 114.6 512 256C512 397.4 '
    + "397.4 512 256 512C201.7 512 151.2 495 109.7 466.1C95.2 455.1 91.64 436 1"
    + "01.8 421.5C111.9 407 131.8 403.5 146.3 413.6C177.4 435.3 215.2 448 256 4"
    + "48C362 448 448 362 448 256C448 149.1 362 64 256 64C202.1 64 155 85.46 12"
    + "0.2 120.2L151 151C166.1 166.1 155.4 192 134.1 192H24C10.75 192 0 181.3 0"
    + " 168V57.94C0 36.56 25.85 25.85 40.97 40.97L74.98 74.98C121.3 28.69 185.3"
    + " 0 255.1 0L256 0zM256 128C269.3 128 280 138.7 280 152V246.1L344.1 311C35"
    + "4.3 320.4 354.3 335.6 344.1 344.1C335.6 354.3 320.4 354.3 311 344.1L239 "
    + "272.1C234.5 268.5 232 262.4 232 256V152C232 138.7 242.7 128 256 128V128z"
    + f'"{ICON_COLOR}/></svg>&nbsp;&nbsp;&nbsp;Logs'
)

swagger_label_with_icon = (
    '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 32 32"'
    + f'{ICON_DIMENSIONS}><path d="M16 0c-8.823 0-16 7.177-16 16s7.177 16 16 16'
    + "c8.823 0 16-7.177 16-16s-7.177-16-16-16zM16 1.527c7.995 0 14.473 6.479 1"
    + "4.473 14.473s-6.479 14.473-14.473 14.473c-7.995 0-14.473-6.479-14.473-14"
    + ".473s6.479-14.473 14.473-14.473zM11.161 7.823c-0.188-0.005-0.375 0-0.568"
    + " 0.005-1.307 0.079-2.093 0.693-2.312 1.964-0.151 0.891-0.125 1.796-0.188"
    + " 2.692-0.020 0.464-0.067 0.928-0.156 1.38-0.177 0.813-0.525 1.068-1.353 "
    + "1.109-0.111 0.011-0.22 0.032-0.324 0.057v1.948c1.5 0.073 1.704 0.605 1.8"
    + "23 2.172 0.048 0.573-0.015 1.147 0.021 1.719 0.027 0.543 0.099 1.079 0.2"
    + "08 1.6 0.344 1.432 1.745 1.911 3.433 1.624v-1.713c-0.272 0-0.511 0.005-0"
    + ".74 0-0.579-0.016-0.792-0.161-0.844-0.713-0.079-0.713-0.057-1.437-0.099-"
    + "2.156-0.089-1.339-0.235-2.651-1.541-3.5 0.672-0.495 1.161-1.084 1.312-1."
    + "865 0.109-0.547 0.177-1.099 0.219-1.651s-0.025-1.12 0.021-1.667c0.077-0."
    + "885 0.135-1.249 1.197-1.213 0.161 0 0.317-0.021 0.495-0.036v-1.745c-0.21"
    + "3 0-0.411-0.005-0.604-0.011zM21.287 7.839c-0.365-0.011-0.729 0.016-1.089"
    + " 0.079v1.697c0.329 0 0.584 0 0.833 0.005 0.439 0.005 0.772 0.177 0.813 0"
    + ".661 0.041 0.443 0.041 0.891 0.083 1.339 0.089 0.896 0.136 1.796 0.292 2"
    + ".677 0.136 0.724 0.636 1.265 1.255 1.713-1.088 0.729-1.411 1.776-1.463 2"
    + ".953-0.032 0.801-0.052 1.615-0.093 2.427-0.037 0.74-0.297 0.979-1.043 0."
    + "995-0.208 0.011-0.411 0.027-0.64 0.041v1.74c0.432 0 0.833 0.027 1.235 0 "
    + "1.239-0.073 1.995-0.677 2.239-1.885 0.104-0.661 0.167-1.333 0.183-2.005 "
    + "0.041-0.615 0.036-1.235 0.099-1.844 0.093-0.953 0.532-1.349 1.484-1.411 "
    + "0.089-0.011 0.177-0.032 0.267-0.057v-1.953c-0.161-0.021-0.271-0.037-0.39"
    + "1-0.041-0.713-0.032-1.068-0.272-1.251-0.948-0.109-0.433-0.177-0.876-0.19"
    + "7-1.324-0.052-0.823-0.047-1.656-0.099-2.479-0.109-1.588-1.063-2.339-2.51"
    + "6-2.38zM12.099 14.875c-1.432 0-1.536 2.109-0.115 2.245h0.079c0.609 0.036"
    + " 1.131-0.427 1.167-1.037v-0.061c0.011-0.62-0.484-1.136-1.104-1.147zM15.9"
    + "79 14.875c-0.593-0.020-1.093 0.448-1.115 1.043 0 0.036 0 0.067 0.005 0.1"
    + "04 0 0.672 0.459 1.099 1.147 1.099 0.677 0 1.104-0.443 1.104-1.136-0.005"
    + "-0.672-0.459-1.115-1.141-1.109zM19.927 14.875c-0.624-0.011-1.145 0.485-1"
    + ".167 1.115 0 0.625 0.505 1.131 1.136 1.131h0.011c0.567 0.099 1.135-0.448"
    + f' 1.172-1.104 0.031-0.609-0.521-1.141-1.152-1.141z"{ICON_COLOR}/></svg>&'
    + "nbsp;&nbsp;&nbsp;Swagger"
)

redoc_label_with_icon = (
    f'<svg xmlns="http://www.w3.org/2000/svg" version="1.0" {ICON_DIMENSIONS} vi'
    + 'ewBox="0 0 100.000000 100.000000" preserveAspectRatio="xMidYMid meet"><g'
    + ' xmlns="http://www.w3.org/2000/svg" transform="translate(0.000000,100.00'
    + '0000) scale(0.100000,-0.100000)" fill="#000000" stroke="none"><path d="M'
    + "83 969 c-30 -15 -48 -33 -62 -63 -20 -40 -21 -60 -21 -416 0 -352 1 -376 2"
    + "0 -415 37 -76 28 -75 468 -75 l391 0 20 26 c38 49 29 78 -51 160 -39 41 -6"
    + "9 76 -67 78 2 2 18 10 34 19 51 26 116 99 149 167 28 58 31 74 31 155 -1 1"
    + "21 -28 189 -104 265 -61 61 -125 96 -203 110 -28 6 -166 10 -307 10 -239 0"
    + " -259 -1 -298 -21z m651 -59 c69 -26 134 -83 171 -151 27 -49 30 -62 30 -1"
    + "49 0 -79 -4 -103 -23 -142 -27 -55 -92 -122 -142 -148 l-37 -19 -223 224 -"
    + "223 223 -89 4 c-84 3 -91 5 -114 31 -33 38 -32 86 2 121 l27 26 283 0 c260"
    + " 0 288 -2 338 -20z m-559 -208 l80 -3 303 -302 c221 -221 302 -307 300 -32"
    + "2 -3 -20 -12 -20 -374 -23 l-371 -2 -27 26 -26 27 0 309 c0 292 1 310 18 3"
    + "02 9 -4 53 -10 97 -12z M120 495 l0 -26 113 3 c104 3 112 4 112 23 0 19 -8"
    + " 20 -112 23 l-113 3 0 -26z M120 375 l0 -25 168 2 c159 3 167 4 167 23 0 1"
    + "9 -8 20 -167 23 l-168 2 0 -25z M120 255 l0 -25 228 2 c219 3 227 4 227 23"
    + f' 0 19 -8 20 -227 23 l-228 2 0 -25z"{ICON_COLOR}/></g></svg>&nbsp;&nbsp;'
    + "&nbsp;Redoc"
)

black_list_with_icon = (
    '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 512 512"'
    f'{ICON_DIMENSIONS}><path d="M0 256C0 114.6 114.6 0 256 0C397.4 0 512 114.6'
    + " 512 256C512 397.4 397.4 512 256 512C114.6 512 0 397.4 0 256zM175 208.1L"
    + "222.1 255.1L175 303C165.7 312.4 165.7 327.6 175 336.1C184.4 346.3 199.6 "
    + "346.3 208.1 336.1L255.1 289.9L303 336.1C312.4 346.3 327.6 346.3 336.1 33"
    + "6.1C346.3 327.6 346.3 312.4 336.1 303L289.9 255.1L336.1 208.1C346.3 199."
    + "6 346.3 184.4 336.1 175C327.6 165.7 312.4 165.7 303 175L255.1 222.1L208."
    + "1 175C199.6 165.7 184.4 165.7 175 175C165.7 184.4 165.7 199.6 175 208.1V"
    + f'208.1z"{ICON_COLOR}/></svg>&nbsp;&nbsp;&nbsp;Blacklist'
)

notification_with_icon = (
    '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 512 512"'
    + f'{ICON_DIMENSIONS}><path d="M480 179.6C498.6 188.4 512 212.1 512 240C512'
    + " 267.9 498.6 291.6 480 300.4V448C480 460.9 472.2 472.6 460.2 477.6C448.3"
    + " 482.5 434.5 479.8 425.4 470.6L381.7 426.1C333.7 378.1 268.6 352 200.7 3"
    + "52H192V480C192 497.7 177.7 512 160 512H96C78.33 512 64 497.7 64 480V352C"
    + "28.65 352 0 323.3 0 288V192C0 156.7 28.65 128 64 128H200.7C268.6 128 333"
    + ".7 101 381.7 53.02L425.4 9.373C434.5 .2215 448.3-2.516 460.2 2.437C472.2"
    + " 7.39 480 19.06 480 32V179.6zM200.7 192H192V288H200.7C280.5 288 357.2 31"
    + f'7.8 416 371.3V108.7C357.2 162.2 280.5 192 200.7 192V192z"{ICON_COLOR}/>'
    + "</svg>&nbsp;&nbsp;&nbsp;Notification"
)
